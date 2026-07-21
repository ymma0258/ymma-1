# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.4 | 0.000% | 8.287109 | 0.000% | 0.265424 | 2.347574 | 0.157206 | 0.864645 | 88.202% |
| 0.25 | 0 | 143584.5 | 6.783% | 5.048242 | 39.083% | 0.140067 | 1.489748 | 0.202696 | 0.843876 | 85.065% |
| 0.5 | 0 | 149827.8 | 11.426% | 4.096932 | 50.563% | 0.119076 | 1.338837 | 0.251341 | 0.820630 | 82.033% |
| 1 | 0 | 159290.9 | 18.463% | 2.858310 | 65.509% | 0.076306 | 0.893960 | 0.252451 | 0.773509 | 75.177% |
| 2 | 0 | 174198.8 | 29.550% | 2.230757 | 73.082% | 0.050733 | 0.809241 | 0.277334 | 0.723420 | 68.323% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
