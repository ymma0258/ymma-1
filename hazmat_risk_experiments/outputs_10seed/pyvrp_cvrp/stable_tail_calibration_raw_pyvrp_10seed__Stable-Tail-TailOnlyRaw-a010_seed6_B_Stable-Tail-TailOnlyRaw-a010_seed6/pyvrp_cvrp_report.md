# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 9.511876 | 0.000% | 0.282381 | 3.263775 | 0.239098 | 0.872871 | 89.853% |
| 0.25 | 0 | 158061.4 | 7.332% | 7.974545 | 16.162% | 0.205756 | 2.606451 | 0.237341 | 0.872182 | 89.457% |
| 0.5 | 0 | 168734.7 | 14.580% | 6.594644 | 30.669% | 0.170938 | 2.417671 | 0.282603 | 0.863676 | 87.532% |
| 1 | 0 | 181658.7 | 23.356% | 4.469718 | 53.009% | 0.113829 | 1.564457 | 0.289430 | 0.834520 | 82.236% |
| 2 | 0 | 202291.6 | 37.367% | 3.887492 | 59.130% | 0.101062 | 1.485771 | 0.346162 | 0.824549 | 80.126% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
