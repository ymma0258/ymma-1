# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.849915 | 0.000% | 0.235421 | 2.458468 | 0.193165 | 0.829028 | 86.144% |
| 1 | 0 | 177573.8 | 21.020% | 3.628815 | 53.773% | 0.084425 | 1.076386 | 0.213134 | 0.719453 | 72.027% |
| 1 | 1 | 189454.3 | 29.117% | 2.663153 | 66.074% | 0.048647 | 0.849735 | 0.227986 | 0.636048 | 61.706% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
