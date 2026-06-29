# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 15.214815 | 0.000% | 0.284735 | 4.026758 | 0.138805 | 0.831603 | 87.468% |
| 1 | 0 | 164758.3 | 22.956% | 6.592498 | 56.671% | 0.063326 | 2.581380 | 0.335066 | 0.758846 | 76.450% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
