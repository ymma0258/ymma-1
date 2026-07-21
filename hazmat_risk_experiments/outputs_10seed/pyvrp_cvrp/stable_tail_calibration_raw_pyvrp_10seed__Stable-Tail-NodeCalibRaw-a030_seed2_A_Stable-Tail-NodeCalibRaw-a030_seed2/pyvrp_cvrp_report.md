# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134065.0 | 0.000% | 8.891213 | 0.000% | 0.295003 | 2.728427 | 0.190263 | 0.875897 | 89.304% |
| 0.25 | 0 | 142468.6 | 6.268% | 6.081832 | 31.597% | 0.175971 | 2.093466 | 0.261767 | 0.866647 | 87.911% |
| 0.5 | 0 | 148416.0 | 10.705% | 4.806755 | 45.938% | 0.136296 | 1.812807 | 0.266878 | 0.852458 | 85.384% |
| 1 | 0 | 157807.9 | 17.710% | 3.337834 | 62.459% | 0.083137 | 1.308290 | 0.313155 | 0.817160 | 79.800% |
| 2 | 0 | 171619.1 | 28.012% | 2.873933 | 67.677% | 0.062741 | 1.208791 | 0.338766 | 0.792909 | 76.045% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
