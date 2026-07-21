# Calibration interpretation

- Best core-ranked calibration: **Stable-Tail-TailOnlyRaw-a030** (method=tail_only_correction, alpha=0.3, rho=0.2).
- Against Stable-Tail GNN on the A/B average, the winner improves all six metrics.
- Against GraphSAGE-TEG-Gate on the A/B average, the winner improves all six metrics.
- Best CVaR95 calibration: **Stable-Tail-TailOnlyRaw-a030**.
- Tail-risk trade-off models against Stable-Tail GNN: none.
- Set A best mean-rank calibration(s): **Stable-Tail-TailOnlyRaw-a030**; against Stable-Tail GNN, Stable-Tail-TailOnlyRaw-a030 improves all six metrics; against GraphSAGE-TEG-Gate, it improves cvar95_aubrc.
- Set B best mean-rank calibration(s): **Stable-Tail-EdgeTailRaw-a005**, **Stable-Tail-EdgeTailRaw-a010**; against Stable-Tail GNN, Stable-Tail-EdgeTailRaw-a005 improves all six metrics; against GraphSAGE-TEG-Gate, it improves all six metrics.
