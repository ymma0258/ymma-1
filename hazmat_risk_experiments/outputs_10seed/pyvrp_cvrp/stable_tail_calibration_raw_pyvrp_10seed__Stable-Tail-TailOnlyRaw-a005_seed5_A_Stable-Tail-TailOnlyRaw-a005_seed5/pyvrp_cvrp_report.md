# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.8 | 0.000% | 7.670058 | 0.000% | 0.240196 | 2.201670 | 0.175025 | 0.875042 | 89.250% |
| 0.25 | 0 | 142557.4 | 6.071% | 5.513173 | 28.121% | 0.156073 | 1.623333 | 0.164760 | 0.864603 | 87.410% |
| 0.5 | 0 | 148086.1 | 10.185% | 3.732633 | 51.335% | 0.109848 | 1.375145 | 0.309920 | 0.829902 | 82.099% |
| 1 | 0 | 156117.4 | 16.161% | 2.566189 | 66.543% | 0.067524 | 0.940523 | 0.269196 | 0.777586 | 74.561% |
| 2 | 0 | 167184.2 | 24.395% | 1.913816 | 75.048% | 0.042222 | 0.632029 | 0.249691 | 0.719647 | 66.055% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
