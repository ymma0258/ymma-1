# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 10.107480 | 0.000% | 0.337053 | 3.160106 | 0.186917 | 0.883427 | 90.640% |
| 0.25 | 0 | 142276.7 | 5.862% | 6.623540 | 34.469% | 0.197299 | 2.359621 | 0.281750 | 0.877026 | 89.193% |
| 0.5 | 0 | 148447.8 | 10.454% | 5.219238 | 48.363% | 0.157001 | 1.778157 | 0.269149 | 0.864860 | 86.656% |
| 1 | 0 | 157528.1 | 17.210% | 3.842496 | 61.984% | 0.108337 | 1.470767 | 0.304796 | 0.838161 | 82.536% |
| 2 | 0 | 171641.4 | 27.711% | 3.226106 | 68.082% | 0.079645 | 1.422842 | 0.365015 | 0.815709 | 78.810% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
