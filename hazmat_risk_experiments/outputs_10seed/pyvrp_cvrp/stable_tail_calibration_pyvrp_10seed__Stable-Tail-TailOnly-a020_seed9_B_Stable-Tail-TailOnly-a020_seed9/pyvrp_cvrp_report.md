# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.268642 | 0.000% | 0.293719 | 2.952639 | 0.219869 | 0.873877 | 90.279% |
| 0.25 | 0 | 157864.4 | 7.393% | 7.821482 | 15.614% | 0.227089 | 2.628910 | 0.229542 | 0.870697 | 89.497% |
| 0.5 | 0 | 167410.0 | 13.886% | 5.124479 | 44.712% | 0.137170 | 1.622487 | 0.262261 | 0.849721 | 85.259% |
| 1 | 0 | 178602.8 | 21.501% | 3.450568 | 62.772% | 0.073424 | 1.283207 | 0.310801 | 0.812014 | 79.228% |
| 2 | 0 | 195032.5 | 32.678% | 3.038919 | 67.213% | 0.058903 | 0.973284 | 0.252958 | 0.791308 | 76.157% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
