# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.1 | 0.000% | 8.778186 | 0.000% | 0.264684 | 2.719459 | 0.197762 | 0.875928 | 89.481% |
| 0.25 | 0 | 156312.6 | 6.193% | 7.435836 | 15.292% | 0.212773 | 2.392224 | 0.225188 | 0.870512 | 88.210% |
| 0.5 | 0 | 164568.0 | 11.801% | 5.660431 | 35.517% | 0.147242 | 2.142346 | 0.317688 | 0.853751 | 85.382% |
| 1 | 0 | 174988.2 | 18.880% | 3.784605 | 56.886% | 0.094377 | 1.649777 | 0.342347 | 0.817862 | 79.690% |
| 2 | 0 | 191260.5 | 29.935% | 3.207244 | 63.463% | 0.069434 | 1.257132 | 0.301158 | 0.800288 | 76.815% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
