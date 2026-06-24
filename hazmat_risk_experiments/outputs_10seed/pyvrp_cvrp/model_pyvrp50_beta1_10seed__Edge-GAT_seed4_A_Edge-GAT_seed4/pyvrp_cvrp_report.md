# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.251542 | 0.000% | 0.256024 | 2.445780 | 0.161866 | 0.866119 | 89.403% |
| 1 | 0 | 161633.0 | 20.624% | 3.472934 | 57.912% | 0.079812 | 1.164323 | 0.275741 | 0.805822 | 79.546% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
