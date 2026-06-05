# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.331368 | 0.000% | 0.255072 | 2.749127 | 0.223233 | 0.838507 | 86.800% |
| 1 | 0 | 178197.8 | 21.611% | 3.566803 | 57.188% | 0.081324 | 1.230389 | 0.239297 | 0.708640 | 70.043% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
