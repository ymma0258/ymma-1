# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.406688 | 0.000% | 0.226655 | 2.752095 | 0.219798 | 0.841198 | 87.350% |
| 1 | 0 | 178489.2 | 21.810% | 3.490541 | 58.479% | 0.070742 | 1.226546 | 0.248276 | 0.712400 | 70.673% |
| 1 | 0.5 | 185640.0 | 26.690% | 3.102491 | 63.095% | 0.059673 | 1.086336 | 0.243701 | 0.680675 | 66.811% |
| 1 | 1 | 190695.0 | 30.140% | 2.728791 | 67.540% | 0.049866 | 1.029187 | 0.284229 | 0.640705 | 62.075% |
| 1 | 2 | 199781.4 | 36.341% | 2.596079 | 69.119% | 0.047114 | 0.972093 | 0.291124 | 0.631965 | 60.627% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
