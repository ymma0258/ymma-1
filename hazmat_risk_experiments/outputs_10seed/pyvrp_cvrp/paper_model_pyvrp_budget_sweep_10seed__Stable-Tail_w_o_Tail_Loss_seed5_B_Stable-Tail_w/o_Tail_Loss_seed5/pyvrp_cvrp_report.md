# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.4 | 0.000% | 7.428047 | 0.000% | 0.221452 | 2.638961 | 0.245755 | 0.871362 | 90.109% |
| 0.25 | 0 | 157029.9 | 6.584% | 6.173845 | 16.885% | 0.152633 | 2.038835 | 0.210437 | 0.871438 | 89.351% |
| 0.5 | 0 | 166490.6 | 13.005% | 5.054597 | 31.953% | 0.129573 | 1.560481 | 0.220677 | 0.867058 | 87.513% |
| 1 | 0 | 178471.2 | 21.137% | 3.380196 | 54.494% | 0.089045 | 1.094582 | 0.234303 | 0.837763 | 82.160% |
| 2 | 0 | 196729.5 | 33.529% | 2.737409 | 63.148% | 0.067396 | 0.957887 | 0.304487 | 0.813307 | 77.488% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
