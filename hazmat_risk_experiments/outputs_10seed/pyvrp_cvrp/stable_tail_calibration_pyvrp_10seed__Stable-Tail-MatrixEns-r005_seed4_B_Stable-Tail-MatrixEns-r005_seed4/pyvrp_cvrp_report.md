# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.5 | 0.000% | 7.913848 | 0.000% | 0.239315 | 2.470783 | 0.188809 | 0.872289 | 88.959% |
| 0.25 | 0 | 156392.9 | 6.440% | 6.958869 | 12.067% | 0.197018 | 2.317431 | 0.211798 | 0.870335 | 88.436% |
| 0.5 | 0 | 164854.9 | 12.199% | 4.911939 | 37.932% | 0.128578 | 1.637862 | 0.246760 | 0.843927 | 83.926% |
| 1 | 0 | 175399.8 | 19.376% | 3.590215 | 54.634% | 0.090625 | 1.476516 | 0.312823 | 0.817111 | 79.552% |
| 2 | 0 | 192008.0 | 30.679% | 2.963976 | 62.547% | 0.059446 | 1.115182 | 0.298221 | 0.798499 | 76.627% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
