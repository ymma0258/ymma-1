# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 6.148965 | 0.000% | 0.191313 | 2.001997 | 0.217184 | 0.873985 | 88.927% |
| 0.25 | 0 | 156246.9 | 6.341% | 5.357396 | 12.873% | 0.134640 | 1.818106 | 0.236344 | 0.871710 | 88.512% |
| 0.5 | 0 | 164616.6 | 12.037% | 3.788664 | 38.385% | 0.090228 | 1.142161 | 0.204790 | 0.842165 | 83.865% |
| 1 | 0 | 175132.2 | 19.194% | 2.858522 | 53.512% | 0.069198 | 1.091196 | 0.313332 | 0.818454 | 79.858% |
| 2 | 0 | 190980.6 | 29.980% | 2.219036 | 63.912% | 0.053902 | 0.722734 | 0.276655 | 0.793474 | 75.267% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
