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
