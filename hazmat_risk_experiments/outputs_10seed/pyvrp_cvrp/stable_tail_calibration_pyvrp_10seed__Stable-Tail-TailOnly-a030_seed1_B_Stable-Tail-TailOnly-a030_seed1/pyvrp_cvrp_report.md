# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 10.281065 | 0.000% | 0.326561 | 3.656872 | 0.267618 | 0.876883 | 90.407% |
| 0.25 | 0 | 155559.6 | 5.825% | 7.951142 | 22.662% | 0.199683 | 2.777795 | 0.266845 | 0.871366 | 88.684% |
| 0.5 | 0 | 163216.2 | 11.033% | 7.340527 | 28.601% | 0.190799 | 2.308821 | 0.224543 | 0.868330 | 87.959% |
| 1 | 0 | 172562.7 | 17.392% | 4.037552 | 60.728% | 0.093252 | 1.416535 | 0.237361 | 0.817322 | 79.522% |
| 2 | 0 | 186008.3 | 26.539% | 3.444875 | 66.493% | 0.068093 | 1.280736 | 0.295357 | 0.802973 | 76.811% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
