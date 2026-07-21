# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.4 | 0.000% | 6.426552 | 0.000% | 0.204237 | 1.983204 | 0.195914 | 0.872188 | 90.168% |
| 0.25 | 0 | 158082.4 | 7.444% | 5.593835 | 12.957% | 0.164650 | 1.825614 | 0.216715 | 0.872603 | 89.936% |
| 0.5 | 0 | 167910.7 | 14.124% | 3.761268 | 41.473% | 0.100618 | 1.286386 | 0.284790 | 0.850551 | 85.680% |
| 1 | 0 | 179535.8 | 22.025% | 2.457147 | 61.766% | 0.054442 | 0.755801 | 0.237264 | 0.809794 | 78.954% |
| 2 | 0 | 196279.5 | 33.405% | 2.188309 | 65.949% | 0.042816 | 0.674692 | 0.227851 | 0.796614 | 76.837% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
