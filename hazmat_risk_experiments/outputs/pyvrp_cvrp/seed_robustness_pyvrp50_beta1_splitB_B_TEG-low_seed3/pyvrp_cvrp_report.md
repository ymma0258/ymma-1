# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 7.707666 | 0.000% | 0.223743 | 2.588108 | 0.218233 | 0.825691 | 85.944% |
| 1 | 0 | 177110.2 | 20.869% | 3.920840 | 49.131% | 0.090530 | 1.080376 | 0.178703 | 0.732446 | 73.718% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
