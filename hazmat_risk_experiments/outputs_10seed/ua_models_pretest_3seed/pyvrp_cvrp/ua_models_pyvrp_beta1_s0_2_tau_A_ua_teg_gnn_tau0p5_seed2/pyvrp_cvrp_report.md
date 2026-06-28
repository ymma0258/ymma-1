# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 11.106663 | 0.000% | 0.372197 | 2.771143 | 0.101819 | 0.819659 | 85.936% |
| 1 | 0 | 162221.3 | 21.063% | 5.793103 | 47.841% | 0.162423 | 1.843189 | 0.185187 | 0.761221 | 78.125% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
