# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.3 | 0.000% | 8.382118 | 0.000% | 0.240259 | 2.622257 | 0.213253 | 0.863118 | 88.789% |
| 0.25 | 0 | 157998.2 | 7.241% | 7.006788 | 16.408% | 0.172395 | 2.131839 | 0.190418 | 0.859235 | 88.462% |
| 0.5 | 0 | 167231.1 | 13.508% | 5.513551 | 34.222% | 0.142378 | 1.925652 | 0.246634 | 0.845857 | 85.809% |
| 1 | 0 | 180413.9 | 22.455% | 3.862728 | 53.917% | 0.100702 | 1.318987 | 0.271616 | 0.813775 | 80.568% |
| 2 | 0 | 200159.9 | 35.858% | 3.189262 | 61.952% | 0.075347 | 1.068396 | 0.280788 | 0.788780 | 76.514% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
