# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.339548 | 0.000% | 0.242076 | 2.653866 | 0.207785 | 0.836548 | 86.597% |
| 1 | 0 | 176257.9 | 20.123% | 3.953627 | 52.592% | 0.078281 | 1.184048 | 0.191167 | 0.738341 | 73.969% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
