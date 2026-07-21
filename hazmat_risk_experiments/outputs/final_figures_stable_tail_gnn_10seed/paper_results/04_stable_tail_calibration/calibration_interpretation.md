# Calibration interpretation

- Best core-ranked calibration: **Stable-Tail-MatrixEns-r010** (method=risk_matrix_ensemble, alpha=0.1, rho=0.1).
- Against Stable-Tail GNN on the A/B average, the winner improves all six metrics.
- Against GraphSAGE-TEG-Gate on the A/B average, the winner improves all six metrics.
- Best CVaR95 calibration: **Stable-Tail-MatrixEns-r010**.
- Tail-risk trade-off models against Stable-Tail GNN: none.
- Set A best mean-rank calibration(s): **Stable-Tail-NodeCalib-a005**; against Stable-Tail GNN, Stable-Tail-NodeCalib-a005 improves avg_risk_at_b, cvar90_aubrc, load_cvar90_aubrc, max_vehicle_cvar90_aubrc; against GraphSAGE-TEG-Gate, it improves none of the six metrics.
- Set B best mean-rank calibration(s): **Stable-Tail-NodeCalib-a030**; against Stable-Tail GNN, Stable-Tail-NodeCalib-a030 improves all six metrics; against GraphSAGE-TEG-Gate, it improves all six metrics.
