# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 4.827518 | 0.000% | 0.147401 | 1.579311 | 0.217884 | 0.878013 | 89.545% |
| 0.25 | 0 | 156230.7 | 6.185% | 4.187869 | 13.250% | 0.104596 | 1.322963 | 0.217778 | 0.875489 | 89.023% |
| 0.5 | 0 | 164723.0 | 11.957% | 3.124842 | 35.270% | 0.074022 | 1.069351 | 0.263038 | 0.849938 | 84.938% |
| 1 | 0 | 174991.1 | 18.936% | 2.235419 | 53.694% | 0.055226 | 0.734625 | 0.272360 | 0.824228 | 80.599% |
| 2 | 0 | 190356.9 | 29.380% | 1.726353 | 64.239% | 0.041960 | 0.543305 | 0.262305 | 0.798884 | 75.961% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
