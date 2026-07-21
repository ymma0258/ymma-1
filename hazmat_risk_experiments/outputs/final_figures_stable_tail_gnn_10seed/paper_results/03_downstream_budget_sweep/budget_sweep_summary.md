# Downstream budget sweep (B = 10%–40%)

All values are lower-is-better. AUBRC uses the trapezoidal rule on B = [0.10, 0.15, ..., 0.40].

| Model | Avg Risk@B | Common AUBRC | CVaR90 AUBRC | CVaR95 AUBRC | LoadCVaR90 AUBRC | MaxVehCVaR90 AUBRC |
|---|---:|---:|---:|---:|---:|---:|
| GCN | 4.2174 | 1.2433 | 0.0308 | 0.0564 | 0.0180 | 0.0553 |
| GAT | 4.4530 | 1.3162 | 0.0330 | 0.0608 | 0.0195 | 0.0596 |
| GraphSAGE | 4.1458 | 1.2170 | 0.0298 | 0.0545 | 0.0179 | 0.0530 |
| SGFormer-adapted | 4.1511 | 1.2218 | 0.0298 | 0.0551 | 0.0175 | 0.0533 |
| Gradformer-adapted | 4.3731 | 1.2899 | 0.0321 | 0.0594 | 0.0189 | 0.0574 |
| Stable-Tail GNN | 4.0571 | 1.1892 | 0.0288 | 0.0525 | 0.0173 | 0.0518 |
| Stable-Tail-Gate | 4.1335 | 1.2106 | 0.0298 | 0.0540 | 0.0174 | 0.0534 |
| SGFormer-TEG-Gate | 4.0533 | 1.1855 | 0.0288 | 0.0528 | 0.0170 | 0.0519 |

## Ablation and extension models

| Model | Avg Risk@B | Common AUBRC | CVaR90 AUBRC | CVaR95 AUBRC | LoadCVaR90 AUBRC | MaxVehCVaR90 AUBRC |
|---|---:|---:|---:|---:|---:|---:|
| TEG-only | 4.1927 | 1.2354 | 0.0303 | 0.0552 | 0.0182 | 0.0546 |
| Stable-Tail w/o Tail Loss | 4.1996 | 1.2350 | 0.0304 | 0.0558 | 0.0183 | 0.0542 |
| GraphSAGE-TEG-Concat | 4.1187 | 1.2105 | 0.0295 | 0.0541 | 0.0176 | 0.0526 |
| GraphSAGE-TEG-Gate | 4.0313 | 1.1853 | 0.0289 | 0.0522 | 0.0168 | 0.0518 |
| SGFormer-TEG-Concat | 4.0872 | 1.2001 | 0.0289 | 0.0530 | 0.0169 | 0.0506 |
