# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 11.356704 | 0.000% | 0.207798 | 3.732681 | 0.197586 | 0.861629 | 89.952% |
| 1 | 0 | 179957.0 | 23.072% | 5.831209 | 48.654% | 0.114147 | 2.061836 | 0.264035 | 0.820719 | 82.879% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
