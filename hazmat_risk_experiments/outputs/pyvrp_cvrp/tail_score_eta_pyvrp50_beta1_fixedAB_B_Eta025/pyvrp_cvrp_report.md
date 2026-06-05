# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 10.044642 | 0.000% | 0.175856 | 3.306550 | 0.224241 | 0.843205 | 87.404% |
| 1 | 178127.6 | 21.563% | 4.207804 | 58.109% | 0.075017 | 1.512922 | 0.264389 | 0.717504 | 71.098% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
