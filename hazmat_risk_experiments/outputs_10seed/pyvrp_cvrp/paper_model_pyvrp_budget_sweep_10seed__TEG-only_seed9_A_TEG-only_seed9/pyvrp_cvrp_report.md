# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 8.506461 | 0.000% | 0.269663 | 2.524862 | 0.183374 | 0.846326 | 87.061% |
| 0.25 | 0 | 142726.2 | 6.197% | 5.462190 | 35.788% | 0.147136 | 1.955988 | 0.254221 | 0.816784 | 83.051% |
| 0.5 | 0 | 148715.1 | 10.653% | 4.385464 | 48.445% | 0.116451 | 1.642884 | 0.266554 | 0.784626 | 79.216% |
| 1 | 0 | 157571.6 | 17.243% | 3.143550 | 63.045% | 0.076600 | 0.896891 | 0.175003 | 0.714256 | 70.785% |
| 2 | 0 | 171884.2 | 27.892% | 2.497027 | 70.646% | 0.048914 | 0.724348 | 0.176140 | 0.650594 | 62.455% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
