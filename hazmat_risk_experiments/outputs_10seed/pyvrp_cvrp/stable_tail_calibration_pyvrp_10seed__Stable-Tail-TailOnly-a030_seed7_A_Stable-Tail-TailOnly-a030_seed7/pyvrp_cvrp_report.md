# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 9.347749 | 0.000% | 0.309117 | 2.672529 | 0.170064 | 0.875888 | 89.889% |
| 0.25 | 0 | 143138.0 | 6.821% | 6.334684 | 32.233% | 0.189989 | 2.070642 | 0.236402 | 0.864819 | 87.579% |
| 0.5 | 0 | 149349.5 | 11.457% | 4.629498 | 50.475% | 0.135714 | 1.620862 | 0.261281 | 0.836689 | 83.278% |
| 1 | 0 | 158276.1 | 18.118% | 3.118933 | 66.634% | 0.082729 | 1.299092 | 0.344559 | 0.792660 | 76.362% |
| 2 | 0 | 171547.4 | 28.022% | 2.620473 | 71.967% | 0.061748 | 0.864715 | 0.257681 | 0.767556 | 72.204% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
