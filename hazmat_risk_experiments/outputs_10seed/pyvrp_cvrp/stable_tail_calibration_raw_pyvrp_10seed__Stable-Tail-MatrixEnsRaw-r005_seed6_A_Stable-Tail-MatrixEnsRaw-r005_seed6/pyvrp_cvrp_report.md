# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 7.325799 | 0.000% | 0.219941 | 2.042730 | 0.148959 | 0.865337 | 88.513% |
| 0.25 | 0 | 143335.0 | 6.862% | 4.599523 | 37.215% | 0.131770 | 1.541085 | 0.251590 | 0.839014 | 84.492% |
| 0.5 | 0 | 149388.6 | 11.375% | 3.826017 | 47.773% | 0.113078 | 1.447979 | 0.305913 | 0.819490 | 81.842% |
| 1 | 0 | 159033.5 | 18.565% | 2.753210 | 62.418% | 0.073649 | 0.852210 | 0.251616 | 0.777637 | 75.796% |
| 2 | 0 | 173827.3 | 29.595% | 2.134998 | 70.856% | 0.048501 | 0.780174 | 0.284727 | 0.724338 | 68.466% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
