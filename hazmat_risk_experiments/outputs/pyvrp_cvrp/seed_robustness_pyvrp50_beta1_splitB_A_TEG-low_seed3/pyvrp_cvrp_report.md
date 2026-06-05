# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 7.356699 | 0.000% | 0.212452 | 2.387266 | 0.193078 | 0.828165 | 85.612% |
| 1 | 0 | 158893.6 | 18.580% | 3.064857 | 58.339% | 0.072872 | 0.954660 | 0.206011 | 0.701349 | 69.212% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
