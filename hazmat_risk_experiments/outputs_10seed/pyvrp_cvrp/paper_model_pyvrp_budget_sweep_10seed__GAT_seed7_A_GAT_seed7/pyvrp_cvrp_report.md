# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 9.075071 | 0.000% | 0.301522 | 2.722852 | 0.176659 | 0.863199 | 89.193% |
| 0.25 | 0 | 142966.4 | 6.428% | 6.435480 | 29.086% | 0.171016 | 1.968538 | 0.207578 | 0.852954 | 87.743% |
| 0.5 | 0 | 149922.2 | 11.606% | 5.136375 | 43.401% | 0.138870 | 1.603223 | 0.198436 | 0.838374 | 85.011% |
| 1 | 0 | 160706.1 | 19.634% | 3.930118 | 56.693% | 0.101180 | 1.299635 | 0.248566 | 0.806079 | 80.457% |
| 2 | 0 | 176803.0 | 31.617% | 3.269682 | 63.971% | 0.077493 | 1.162959 | 0.295051 | 0.781869 | 76.589% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
