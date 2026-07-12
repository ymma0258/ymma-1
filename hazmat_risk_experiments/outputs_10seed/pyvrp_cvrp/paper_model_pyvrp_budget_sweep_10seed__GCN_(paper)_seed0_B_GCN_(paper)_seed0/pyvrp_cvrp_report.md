# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 7.185579 | 0.000% | 0.218093 | 2.360621 | 0.242709 | 0.853337 | 87.564% |
| 0.25 | 0 | 157547.7 | 7.177% | 6.539437 | 8.992% | 0.183543 | 2.072065 | 0.226668 | 0.852284 | 88.010% |
| 0.5 | 0 | 166859.8 | 13.512% | 4.892931 | 31.906% | 0.131073 | 1.583149 | 0.208644 | 0.832559 | 84.769% |
| 1 | 0 | 180489.9 | 22.785% | 3.398690 | 52.701% | 0.074234 | 1.320188 | 0.305388 | 0.800875 | 79.548% |
| 2 | 0 | 198457.9 | 35.008% | 2.622997 | 63.496% | 0.051647 | 0.840208 | 0.246570 | 0.759790 | 73.029% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
