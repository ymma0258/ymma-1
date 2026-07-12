# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.3 | 0.000% | 8.526431 | 0.000% | 0.251227 | 2.764086 | 0.209146 | 0.852908 | 89.059% |
| 0.25 | 0 | 157754.3 | 7.123% | 7.663288 | 10.123% | 0.213184 | 2.439639 | 0.202234 | 0.852871 | 88.807% |
| 0.5 | 0 | 167646.7 | 13.841% | 6.118380 | 28.242% | 0.175212 | 2.006567 | 0.229185 | 0.841114 | 86.485% |
| 1 | 0 | 180469.5 | 22.548% | 4.109869 | 51.798% | 0.087804 | 1.418022 | 0.249305 | 0.802542 | 80.673% |
| 2 | 0 | 199189.6 | 35.260% | 3.196515 | 62.511% | 0.062128 | 1.015014 | 0.260530 | 0.764901 | 74.636% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
