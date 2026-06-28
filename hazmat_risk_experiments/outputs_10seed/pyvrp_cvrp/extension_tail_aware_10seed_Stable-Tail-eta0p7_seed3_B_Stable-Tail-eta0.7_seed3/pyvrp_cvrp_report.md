# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.088028 | 0.000% | 0.172620 | 3.017627 | 0.203717 | 0.871025 | 88.671% |
| 1 | 0 | 174810.6 | 19.137% | 3.614871 | 60.224% | 0.058769 | 1.482522 | 0.319723 | 0.784685 | 74.740% |
| 2 | 0 | 190745.7 | 29.997% | 3.075018 | 66.164% | 0.049096 | 1.271573 | 0.312510 | 0.767989 | 71.711% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
