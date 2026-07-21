# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.8 | 0.000% | 9.747405 | 0.000% | 0.309031 | 3.227231 | 0.246766 | 0.872587 | 89.878% |
| 0.25 | 0 | 156455.4 | 6.338% | 8.042050 | 17.495% | 0.235676 | 2.651299 | 0.244959 | 0.867757 | 88.642% |
| 0.5 | 0 | 164489.7 | 11.798% | 6.819779 | 30.035% | 0.176724 | 2.055292 | 0.216550 | 0.861593 | 87.123% |
| 1 | 0 | 174080.3 | 18.317% | 3.963670 | 59.336% | 0.089833 | 1.375490 | 0.239297 | 0.814290 | 79.164% |
| 2 | 0 | 187847.4 | 27.674% | 3.258404 | 66.572% | 0.066034 | 1.195270 | 0.267966 | 0.794511 | 75.608% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
