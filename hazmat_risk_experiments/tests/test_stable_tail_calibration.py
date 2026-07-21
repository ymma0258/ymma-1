"""Regression tests for Stable-Tail post-processing calibration."""

from __future__ import annotations

import json
import os
import shutil
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

import numpy as np


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

import export_stable_tail_calibrated_risk_matrix as calibration  # noqa: E402
import run_stable_tail_calibration_exports as batch_export  # noqa: E402
import summarize_stable_tail_calibration as summary  # noqa: E402


class StableTailCalibrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.base_risk = np.asarray([0.2, 0.4], dtype=float)
        self.score = np.asarray([0.2, 0.6, 0.8], dtype=float)
        self.p_high = np.asarray([0.4, 0.7, 0.9], dtype=float)
        self.src = np.asarray([0, 1], dtype=int)
        self.dst = np.asarray([1, 2], dtype=int)
        self.w_raw = np.asarray([0.5, 0.8], dtype=float)
        self.w_floor = 0.01 + 0.99 * self.w_raw

    def calibrate(
        self, method: str, mode: str = "raw", threshold: float = 0.5, rho: float = 0.2
    ):
        return calibration.calibrate(
            method,
            self.base_risk,
            self.score,
            self.p_high,
            self.src,
            self.dst,
            self.w_raw,
            self.w_floor,
            0.1,
            rho,
            0.9,
            20.0,
            False,
            mode,
            threshold,
        )

    def test_raw_is_default_formula_without_thresholding(self) -> None:
        raw, _, details = self.calibrate("edge_tail_correction", "raw", 0.95)
        expected_tail = self.w_raw * np.maximum(
            self.p_high[self.src], self.p_high[self.dst]
        )
        np.testing.assert_allclose(raw, self.base_risk * (1 + 0.1 * expected_tail))
        self.assertEqual(details["p_high_mode"], "raw")
        self.assertEqual(details["p_high_raw_mean"], details["p_high_used_mean"])

    def test_gate_threshold_changes_correction(self) -> None:
        disabled, _, _ = self.calibrate("edge_tail_correction", "gate", 0.95)
        active, _, _ = self.calibrate("edge_tail_correction", "gate", 0.5)
        np.testing.assert_allclose(disabled, self.base_risk)
        self.assertTrue(np.any(active > self.base_risk))

    def test_sparse_ensemble_uses_positive_tail_scale(self) -> None:
        risk, _, details = self.calibrate("risk_matrix_ensemble", "gate", 0.5)
        self.assertGreater(details["normalization_scale"], 0)
        self.assertGreater(details["positive_teg_tail_edges"], 0)
        self.assertIsNone(details["ensemble_fallback"])
        self.assertFalse(np.allclose(risk, 0.8 * self.base_risk))

    def test_empty_ensemble_tail_keeps_base(self) -> None:
        risk, _, details = self.calibrate("risk_matrix_ensemble", "gate", 0.95)
        np.testing.assert_allclose(risk, self.base_risk)
        self.assertEqual(details["ensemble_fallback"], "no_active_tail_edges_keep_base")

    def test_cache_signature_includes_parameters_and_source_hashes(self) -> None:
        root = Path(__file__).resolve().parent / ".stable_tail_calibration_test_tmp"
        if root.exists():
            shutil.rmtree(root)
        root.mkdir()
        try:
            base = root / "base"
            output = root / "output"
            base.mkdir()
            output.mkdir()
            for directory in (base, output):
                np.savez(directory / "data_2021_node_risk.npz", scores_norm=[0.2])
                np.savez(directory / "data_2021_edge_risk.npz", R_ij=[0.1])
            (output / "data_2021_edge_risk.csv").write_text("R_ij\n0.1\n", encoding="utf-8")
            args = SimpleNamespace(
                year="data_2021",
                hard_tail=False,
                clip=True,
                tail_quantile=0.9,
                tail_sharpness=20.0,
                p_high_mode="raw",
                p_high_gate_threshold=0.5,
            )
            meta = {
                "schema_version": batch_export.CALIBRATION_SCHEMA_VERSION,
                "method": "edge_tail_correction",
                "alpha": 0.1,
                "rho": 0.2,
                "year": args.year,
                "hard_tail": args.hard_tail,
                "clip": args.clip,
                "tail_quantile": args.tail_quantile,
                "tail_sharpness": args.tail_sharpness,
                "p_high_mode": args.p_high_mode,
                "p_high_gate_threshold": args.p_high_gate_threshold,
                "base_risk_dir": str(base.resolve()),
                "source_fingerprints": batch_export.source_fingerprints(base, args.year),
            }
            (output / "calibration_meta.json").write_text(json.dumps(meta), encoding="utf-8")
            self.assertTrue(
                batch_export.complete(output, base, "edge_tail_correction", 0.1, 0.2, "raw", args)
            )
            args.tail_sharpness = 10.0
            self.assertFalse(
                batch_export.complete(output, base, "edge_tail_correction", 0.1, 0.2, "raw", args)
            )
            args.tail_sharpness = 20.0
            np.savez(base / "data_2021_edge_risk.npz", R_ij=[0.2])
            self.assertFalse(
                batch_export.complete(output, base, "edge_tail_correction", 0.1, 0.2, "raw", args)
            )
        finally:
            shutil.rmtree(root)

    def test_core_score_is_mean_of_metric_ranks(self) -> None:
        rows = [
            {"model": "A", "x": 1.0, "y": 3.0},
            {"model": "B", "x": 2.0, "y": 1.0},
            {"model": "C", "x": 3.0, "y": 2.0},
        ]
        scores = summary.mean_rank_scores(rows, ("x", "y"))
        self.assertEqual(min(scores, key=scores.get), "B")
        self.assertEqual(scores["B"], 1.5)

    def test_summary_rejects_stale_downstream_results(self) -> None:
        root = Path(__file__).resolve().parent / ".stable_tail_freshness_test_tmp"
        if root.exists():
            shutil.rmtree(root)
        root.mkdir()
        try:
            risk_dir = root / "risk"
            risk_dir.mkdir()
            risk_file = risk_dir / "data_2021_edge_risk.npz"
            risk_file.write_bytes(b"risk")
            manifest = root / "manifest.csv"
            manifest.write_text(f"risk_dir\n{risk_dir}\n", encoding="utf-8")
            downstream = [root / name for name in ("self.csv", "common.csv", "load.csv")]
            for path in downstream:
                path.write_text("value\n1\n", encoding="utf-8")
                os.utime(path, (1_000, 1_000))
            os.utime(risk_file, (2_000, 2_000))
            args = SimpleNamespace(
                source_manifest=manifest,
                self_summary=downstream[0],
                common_summary=downstream[1],
                load_summary=downstream[2],
            )
            with self.assertRaisesRegex(RuntimeError, "older than the risk matrices"):
                summary.validate_input_freshness(args)
            for path in downstream:
                os.utime(path, (3_000, 3_000))
            summary.validate_input_freshness(args)
        finally:
            shutil.rmtree(root)


if __name__ == "__main__":
    unittest.main()
