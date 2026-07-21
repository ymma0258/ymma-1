# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.884777 | 0.000% | 0.230003 | 2.179789 | 0.145642 | 0.866627 | 88.728% |
| 0.25 | 0 | 143070.6 | 6.718% | 5.074073 | 35.647% | 0.150157 | 1.631589 | 0.254873 | 0.846053 | 85.284% |
| 0.5 | 0 | 149290.5 | 11.357% | 4.041578 | 48.742% | 0.120182 | 1.499098 | 0.286628 | 0.818770 | 81.801% |
| 1 | 0 | 158494.2 | 18.222% | 2.885111 | 63.409% | 0.075702 | 1.054034 | 0.314277 | 0.775093 | 75.379% |
| 2 | 0 | 172908.6 | 28.974% | 2.242232 | 71.563% | 0.052145 | 0.814837 | 0.287196 | 0.728554 | 68.848% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
