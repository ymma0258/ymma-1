# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.7 | 0.000% | 8.403652 | 0.000% | 0.253338 | 2.831992 | 0.244504 | 0.856160 | 89.095% |
| 0.25 | 0 | 157165.1 | 6.675% | 6.832404 | 18.697% | 0.186561 | 2.492331 | 0.249532 | 0.848821 | 87.935% |
| 0.5 | 0 | 166764.8 | 13.191% | 5.951841 | 29.176% | 0.174965 | 1.859198 | 0.192662 | 0.844673 | 86.415% |
| 1 | 0 | 180478.7 | 22.499% | 4.433461 | 47.244% | 0.113848 | 1.510572 | 0.285741 | 0.822182 | 82.475% |
| 2 | 0 | 201333.3 | 36.654% | 3.518154 | 58.135% | 0.072645 | 1.276781 | 0.317722 | 0.799219 | 78.314% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
