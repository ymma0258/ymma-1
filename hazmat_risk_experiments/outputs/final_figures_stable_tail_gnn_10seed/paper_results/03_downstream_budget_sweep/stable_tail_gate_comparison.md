# Stable-Tail-Gate downstream comparison

Difference is Stable-Tail-Gate minus reference; negative values mean lower risk.

| Set | Reference | Avg Risk@B Δ | Common AUBRC Δ | CVaR90 Δ | CVaR95 Δ | LoadCVaR90 Δ | MaxVehCVaR90 Δ |
|---|---|---:|---:|---:|---:|---:|---:|
| A | Stable-Tail GNN | +0.0702 | +0.0119 | +0.00069 | +0.00102 | +0.00008 | -0.00024 |
| A | GraphSAGE-TEG-Gate | +0.1804 | +0.0398 | +0.00131 | +0.00159 | +0.00099 | +0.00197 |
| B | Stable-Tail GNN | +0.0826 | +0.0309 | +0.00117 | +0.00212 | +0.00025 | +0.00350 |
| B | GraphSAGE-TEG-Gate | +0.0240 | +0.0108 | +0.00047 | +0.00214 | +0.00017 | +0.00119 |
| AB | Stable-Tail GNN | +0.0764 | +0.0214 | +0.00093 | +0.00157 | +0.00016 | +0.00163 |
| AB | GraphSAGE-TEG-Gate | +0.1022 | +0.0253 | +0.00089 | +0.00187 | +0.00058 | +0.00158 |
