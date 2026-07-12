# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.7 | 0.000% | 7.436337 | 0.000% | 0.240009 | 2.357154 | 0.207277 | 0.875011 | 88.689% |
| 0.25 | 0 | 142208.0 | 5.916% | 4.679546 | 37.072% | 0.134248 | 1.526686 | 0.219902 | 0.856400 | 85.874% |
| 0.5 | 0 | 147673.4 | 9.987% | 3.672540 | 50.614% | 0.102550 | 1.381634 | 0.279137 | 0.835894 | 82.767% |
| 1 | 0 | 155679.0 | 15.949% | 2.427880 | 67.351% | 0.050170 | 0.739583 | 0.196468 | 0.778184 | 74.534% |
| 2 | 0 | 167142.6 | 24.487% | 1.980126 | 73.372% | 0.038777 | 0.655647 | 0.226534 | 0.742395 | 68.921% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
