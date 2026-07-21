# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.1 | 0.000% | 4.137047 | 0.000% | 0.125367 | 1.290693 | 0.191869 | 0.870455 | 88.615% |
| 0.25 | 0 | 141692.7 | 5.585% | 2.990777 | 27.707% | 0.086036 | 0.967622 | 0.207991 | 0.858910 | 87.075% |
| 0.5 | 0 | 146863.8 | 9.438% | 2.230682 | 46.080% | 0.064629 | 0.808449 | 0.259868 | 0.834876 | 83.388% |
| 1 | 0 | 154807.4 | 15.357% | 1.549871 | 62.537% | 0.041973 | 0.482260 | 0.219451 | 0.782936 | 76.263% |
| 2 | 0 | 166634.6 | 24.171% | 1.295035 | 68.697% | 0.031295 | 0.433159 | 0.282585 | 0.754952 | 71.795% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
