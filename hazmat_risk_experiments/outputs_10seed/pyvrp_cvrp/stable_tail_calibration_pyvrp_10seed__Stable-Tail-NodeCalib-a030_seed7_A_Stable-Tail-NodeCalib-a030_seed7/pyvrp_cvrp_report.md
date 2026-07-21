# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 8.835485 | 0.000% | 0.286584 | 2.543651 | 0.165911 | 0.872210 | 89.270% |
| 0.25 | 0 | 143107.3 | 6.798% | 6.083942 | 31.142% | 0.180957 | 2.021915 | 0.227632 | 0.859974 | 86.912% |
| 0.5 | 0 | 149213.2 | 11.355% | 4.710451 | 46.687% | 0.135097 | 1.592758 | 0.208769 | 0.839377 | 83.725% |
| 1 | 0 | 158544.4 | 18.318% | 3.261987 | 63.081% | 0.077554 | 1.326478 | 0.319297 | 0.796579 | 77.051% |
| 2 | 0 | 171542.0 | 28.018% | 2.586396 | 70.727% | 0.053452 | 0.803661 | 0.243875 | 0.764552 | 71.840% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
