# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.978026 | 0.000% | 0.245737 | 2.325127 | 0.143541 | 0.859189 | 88.702% |
| 1 | 0 | 161189.0 | 20.292% | 3.415302 | 57.191% | 0.078690 | 1.114934 | 0.262483 | 0.777657 | 77.257% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
