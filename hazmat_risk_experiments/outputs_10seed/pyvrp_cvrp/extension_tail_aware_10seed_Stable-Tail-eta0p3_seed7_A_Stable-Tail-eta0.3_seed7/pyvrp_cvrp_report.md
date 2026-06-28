# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 10.711677 | 0.000% | 0.224070 | 3.128982 | 0.153795 | 0.875919 | 89.844% |
| 1 | 0 | 158203.8 | 18.065% | 3.863225 | 63.934% | 0.060911 | 1.459595 | 0.309182 | 0.805833 | 77.376% |
| 2 | 0 | 170870.0 | 27.517% | 3.187685 | 70.241% | 0.045988 | 0.968048 | 0.233118 | 0.775860 | 72.563% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
