# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.194905 | 0.000% | 0.312921 | 3.483250 | 0.247792 | 0.877571 | 90.969% |
| 1 | 0 | 178391.9 | 21.578% | 4.668683 | 54.206% | 0.122078 | 1.768763 | 0.325443 | 0.852807 | 83.899% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
