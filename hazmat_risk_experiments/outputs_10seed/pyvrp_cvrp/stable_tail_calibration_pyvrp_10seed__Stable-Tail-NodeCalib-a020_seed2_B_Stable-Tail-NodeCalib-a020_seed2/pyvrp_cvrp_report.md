# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.876667 | 0.000% | 0.275555 | 3.378144 | 0.308184 | 0.874741 | 89.529% |
| 0.25 | 0 | 156653.7 | 6.569% | 7.822211 | 11.879% | 0.236082 | 3.162941 | 0.325158 | 0.874944 | 89.302% |
| 0.5 | 0 | 165076.8 | 12.299% | 6.279802 | 29.255% | 0.172728 | 2.299538 | 0.270050 | 0.861235 | 86.887% |
| 1 | 0 | 177842.1 | 20.983% | 4.506367 | 49.234% | 0.116458 | 1.820714 | 0.288259 | 0.843549 | 83.371% |
| 2 | 0 | 195751.9 | 33.167% | 3.669457 | 58.662% | 0.088209 | 1.655347 | 0.352103 | 0.826048 | 80.002% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
