# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.4 | 0.000% | 9.819193 | 0.000% | 0.313053 | 3.520740 | 0.276697 | 0.872470 | 90.071% |
| 0.25 | 0 | 156152.0 | 5.988% | 8.204782 | 16.441% | 0.244277 | 2.909026 | 0.258253 | 0.870121 | 88.838% |
| 0.5 | 0 | 164271.4 | 11.499% | 6.861893 | 30.118% | 0.177629 | 2.053902 | 0.193695 | 0.862761 | 87.244% |
| 1 | 0 | 173938.7 | 18.060% | 4.025229 | 59.007% | 0.094767 | 1.476191 | 0.274273 | 0.816254 | 79.632% |
| 2 | 0 | 187934.6 | 27.560% | 3.122617 | 68.199% | 0.060191 | 1.182570 | 0.269150 | 0.788646 | 74.735% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
