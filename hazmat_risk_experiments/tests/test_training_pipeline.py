"""Focused regression tests for training/export consistency fixes."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

import numpy as np
import torch


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import train_risk_model as training  # noqa: E402
import evaluate_route_pool_budget as budget_eval  # noqa: E402
import export_tail_enhanced_risk_matrix as tail_export  # noqa: E402


def graph(year: str, labels: list[int]) -> training.GraphData:
    count = len(labels)
    src = np.arange(count - 1, dtype=np.int64)
    dst = src + 1
    edges = np.concatenate(
        [np.stack([src, dst], axis=0), np.stack([dst, src], axis=0)], axis=1
    )
    return training.GraphData(
        year=year,
        x=torch.arange(count * 3, dtype=torch.float32).reshape(count, 3),
        y=torch.tensor(labels, dtype=torch.long),
        edge_index=torch.from_numpy(edges),
        edge_weight=torch.linspace(0.0, 2.0, edges.shape[1]),
        labeled_idx=np.flatnonzero(np.asarray(labels) > 0),
    )


class TrainingPipelineTests(unittest.TestCase):
    def test_tail_score_uses_high_risk_probability_and_clips(self) -> None:
        scores = np.asarray([0.10, 0.90])
        p_high = np.asarray([0.40, 0.80])
        actual = tail_export.tail_node_scores(scores, p_high, eta=0.5)
        np.testing.assert_allclose(actual, np.asarray([0.30, 1.00]))

    def test_ranking_metrics_reward_high_risk_ordering(self) -> None:
        labels = np.asarray([1, 2, 3, 4, 5, 6, 7, 8, 6, 7])
        scores = labels.astype(float)
        metrics = training.ranking_metrics(labels, scores)
        self.assertEqual(metrics["high_risk_recall_at_top20pct"], 0.4)
        self.assertAlmostEqual(metrics["ndcg_at_top20pct"], 1.0)
        self.assertEqual(metrics["high_risk_hits_at_10"], 5.0)

    def test_budget_selection_uses_shared_shortest_route_baseline(self) -> None:
        rows = [
            {
                "risk_source": "M0",
                "customer_set": "A",
                "seed": 0,
                "beta": 0.0,
                "lambda_concentration": 0.0,
                "pyvrp_cost": 100.0,
                "common_global_risk": 10.0,
                "common_global_cvar90": 5.0,
                "common_global_cvar95": 6.0,
                "load_global_risk": 8.0,
                "load_cvar90": 4.0,
                "common_edge_burden_gini_used": 0.5,
                "common_top10_burden_share": 0.4,
            },
            {
                "risk_source": "M0",
                "customer_set": "A",
                "seed": 0,
                "beta": 1.0,
                "lambda_concentration": 0.0,
                "pyvrp_cost": 125.0,
                "common_global_risk": 4.0,
                "common_global_cvar90": 2.0,
                "common_global_cvar95": 3.0,
                "load_global_risk": 3.0,
                "load_cvar90": 2.0,
                "common_edge_burden_gini_used": 0.3,
                "common_top10_burden_share": 0.2,
            },
        ]
        candidates = budget_eval.assign_cost_increase(rows)
        selected = budget_eval.budget_metric_best(candidates, [0.20, 0.25])
        risk_at_20 = next(
            row for row in selected if row["budget"] == 0.20 and row["selector"] == "common_risk"
        )
        risk_at_25 = next(
            row for row in selected if row["budget"] == 0.25 and row["selector"] == "common_risk"
        )
        self.assertEqual(risk_at_20["selected_value"], 10.0)
        self.assertEqual(risk_at_25["selected_value"], 4.0)

    def test_rerank_score_uses_pool_normalization_for_all_budgets(self) -> None:
        rows = []
        for cost, risk in [(100.0, 10.0), (125.0, 5.0), (130.0, 0.0)]:
            rows.append(
                {
                    "risk_source": "M0",
                    "customer_set": "A",
                    "seed": 0,
                    "pyvrp_cost": cost,
                    "cost_increase_pct": cost / 100.0 - 1.0,
                    "common_global_risk": risk,
                    "common_global_cvar90": risk,
                    "load_global_risk": risk,
                    "common_top10_burden_share": risk / 10.0,
                }
            )
        weights = {"cost": 1.0, "common_risk": 0.0, "cvar90": 0.0, "load_risk": 0.0, "top10_share": 0.0}
        selected = budget_eval.rerank_pool(rows, [0.25, 0.30], weights)
        by_budget = {row["budget"]: row for row in selected}
        self.assertEqual(by_budget[0.25]["pyvrp_cost"], 100.0)
        self.assertEqual(by_budget[0.30]["pyvrp_cost"], 100.0)
        self.assertEqual(by_budget[0.25]["cost_norm"], by_budget[0.30]["cost_norm"])

    def test_split_b_has_disjoint_validation_and_test_sets(self) -> None:
        # Eight samples per class keep every nested stratified subset feasible.
        labels = [level for level in range(1, 9) for _ in range(8)]
        graph20 = graph("data_2020", labels)
        graph21 = graph("data_2021", labels)
        splits = training.build_splits(graph20, graph21, "B", 3, 0.25)
        split21 = splits["data_2021"]
        self.assertGreater(split21["val"].size, 0)
        self.assertFalse(set(split21["train"]) & set(split21["val"]))
        self.assertFalse(set(split21["train"]) & set(split21["test"]))
        self.assertFalse(set(split21["val"]) & set(split21["test"]))
        self.assertEqual(
            split21["train"].size + split21["val"].size + split21["test"].size,
            len(labels),
        )

    def test_shared_preprocessing_reuses_one_edge_scale(self) -> None:
        labels = [1, 2, 3, 4, 5, 6, 7, 8]
        graphs = [graph("data_2020", labels), graph("data_2021", labels)]
        graphs[1].edge_weight *= 10
        splits = {
            item.year: {
                "train": np.arange(4),
                "val": np.arange(4, 6),
                "test": np.arange(6, 8),
            }
            for item in graphs
        }
        state = training.fit_and_apply_preprocessing(
            graphs, splits, "shared_2020", True
        )
        self.assertIsNotNone(state.edge_min)
        self.assertIsNotNone(state.edge_p99)
        self.assertTrue(
            torch.all((graphs[0].edge_weight >= 0) & (graphs[0].edge_weight <= 1))
        )
        self.assertTrue(
            torch.all((graphs[1].edge_weight >= 0) & (graphs[1].edge_weight <= 1))
        )
        fitted = torch.cat([item.x[:4] for item in graphs], dim=0)
        self.assertTrue(torch.allclose(fitted.mean(dim=0), torch.zeros(3), atol=1e-5))

    def test_gate_normalized_messages_sum_to_one_per_destination(self) -> None:
        edge_index = torch.tensor([[0, 1, 2], [2, 2, 2]], dtype=torch.long)
        weights = torch.tensor([0.2, 0.3, 0.5], dtype=torch.float32)
        norm = training.normalize_messages(3, edge_index, weights)
        self.assertAlmostEqual(float(norm.sum()), 1.0, places=6)


if __name__ == "__main__":
    unittest.main()
