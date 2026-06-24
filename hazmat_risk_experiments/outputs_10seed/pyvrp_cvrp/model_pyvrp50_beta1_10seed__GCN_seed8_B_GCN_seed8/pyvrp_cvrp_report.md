# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.190006 | 0.000% | 0.239074 | 2.708218 | 0.216232 | 0.867744 | 88.988% |
| 1 | 0 | 181518.2 | 23.708% | 3.745628 | 54.266% | 0.083203 | 1.531171 | 0.343902 | 0.817083 | 80.293% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
