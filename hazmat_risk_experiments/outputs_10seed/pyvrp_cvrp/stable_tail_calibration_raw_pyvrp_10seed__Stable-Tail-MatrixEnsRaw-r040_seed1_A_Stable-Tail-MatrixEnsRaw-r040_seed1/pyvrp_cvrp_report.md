# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 5.950710 | 0.000% | 0.192148 | 1.697918 | 0.166833 | 0.875050 | 90.147% |
| 0.25 | 0 | 141967.3 | 5.737% | 4.224418 | 29.010% | 0.127583 | 1.258559 | 0.193321 | 0.872487 | 88.897% |
| 0.5 | 0 | 147628.7 | 9.953% | 2.818343 | 52.639% | 0.067409 | 1.011501 | 0.239668 | 0.844292 | 84.142% |
| 1 | 0 | 155973.7 | 16.169% | 1.993840 | 66.494% | 0.046461 | 0.641959 | 0.215023 | 0.798563 | 77.704% |
| 2 | 0 | 168488.8 | 25.490% | 1.609594 | 72.951% | 0.033698 | 0.457636 | 0.222614 | 0.771799 | 73.260% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
