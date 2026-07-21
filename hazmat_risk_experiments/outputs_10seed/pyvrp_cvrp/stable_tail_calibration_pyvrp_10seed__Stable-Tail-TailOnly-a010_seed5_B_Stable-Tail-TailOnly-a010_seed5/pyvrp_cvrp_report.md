# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 7.875964 | 0.000% | 0.245712 | 2.619083 | 0.235400 | 0.875559 | 89.209% |
| 0.25 | 0 | 156450.3 | 6.286% | 6.620080 | 15.946% | 0.175982 | 2.340465 | 0.250502 | 0.871887 | 88.409% |
| 0.5 | 0 | 165138.7 | 12.189% | 4.681835 | 40.555% | 0.112372 | 1.429959 | 0.225585 | 0.842674 | 83.771% |
| 1 | 0 | 175969.0 | 19.546% | 3.531195 | 55.165% | 0.085406 | 1.239708 | 0.279234 | 0.816540 | 79.358% |
| 2 | 0 | 191124.3 | 29.842% | 2.869431 | 63.567% | 0.069299 | 0.932075 | 0.275323 | 0.794819 | 75.634% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
