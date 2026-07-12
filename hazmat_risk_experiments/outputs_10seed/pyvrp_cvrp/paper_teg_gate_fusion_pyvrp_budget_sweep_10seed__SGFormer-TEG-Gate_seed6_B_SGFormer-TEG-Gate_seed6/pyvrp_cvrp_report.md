# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.8 | 0.000% | 10.215610 | 0.000% | 0.300008 | 3.219146 | 0.194145 | 0.853120 | 88.884% |
| 0.25 | 0 | 158826.7 | 8.096% | 9.048246 | 11.427% | 0.219726 | 2.937021 | 0.205410 | 0.851991 | 89.059% |
| 0.5 | 0 | 170465.6 | 16.018% | 7.456835 | 27.005% | 0.200730 | 2.400217 | 0.224513 | 0.844502 | 87.149% |
| 1 | 0 | 186789.0 | 27.127% | 5.617986 | 45.006% | 0.148612 | 2.071960 | 0.295822 | 0.820178 | 83.164% |
| 2 | 0 | 211988.2 | 44.278% | 4.470345 | 56.240% | 0.105789 | 1.657379 | 0.336481 | 0.796841 | 78.978% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
