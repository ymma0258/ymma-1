# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 6.336959 | 0.000% | 0.200339 | 2.012326 | 0.212835 | 0.871853 | 90.043% |
| 0.25 | 0 | 157948.9 | 7.499% | 5.616532 | 11.369% | 0.164625 | 1.871466 | 0.226884 | 0.869418 | 89.740% |
| 0.5 | 0 | 167891.6 | 14.266% | 3.621516 | 42.851% | 0.096735 | 1.303596 | 0.272056 | 0.846660 | 85.239% |
| 1 | 0 | 179026.6 | 21.844% | 2.441532 | 61.472% | 0.054040 | 0.860723 | 0.276654 | 0.810656 | 79.041% |
| 2 | 0 | 196258.3 | 33.572% | 2.127106 | 66.433% | 0.041573 | 0.691653 | 0.257361 | 0.792557 | 76.352% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
