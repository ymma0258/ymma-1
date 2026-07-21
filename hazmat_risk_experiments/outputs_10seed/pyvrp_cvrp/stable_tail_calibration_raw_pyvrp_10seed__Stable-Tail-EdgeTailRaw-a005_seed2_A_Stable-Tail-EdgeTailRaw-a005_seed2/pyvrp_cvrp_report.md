# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 8.953513 | 0.000% | 0.301240 | 2.636363 | 0.177754 | 0.877921 | 90.094% |
| 0.25 | 0 | 142358.0 | 6.028% | 5.684698 | 36.509% | 0.166894 | 2.127680 | 0.283605 | 0.863111 | 87.336% |
| 0.5 | 0 | 148553.0 | 10.642% | 4.765886 | 46.771% | 0.142241 | 1.694862 | 0.248878 | 0.853143 | 85.404% |
| 1 | 0 | 157835.6 | 17.555% | 3.352477 | 62.557% | 0.093142 | 1.283568 | 0.320758 | 0.816866 | 79.733% |
| 2 | 0 | 171891.8 | 28.024% | 2.805846 | 68.662% | 0.065656 | 1.240341 | 0.374590 | 0.791552 | 75.865% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
