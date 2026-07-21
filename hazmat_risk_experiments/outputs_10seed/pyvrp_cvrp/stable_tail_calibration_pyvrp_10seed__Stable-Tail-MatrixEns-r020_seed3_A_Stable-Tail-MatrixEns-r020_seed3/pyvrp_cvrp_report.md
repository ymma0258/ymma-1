# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 5.512947 | 0.000% | 0.162668 | 1.627987 | 0.167889 | 0.871568 | 88.800% |
| 0.25 | 0 | 141812.6 | 5.832% | 4.047738 | 26.578% | 0.116339 | 1.231043 | 0.197195 | 0.860285 | 87.199% |
| 0.5 | 0 | 147056.4 | 9.745% | 2.888353 | 47.608% | 0.081679 | 0.953652 | 0.237450 | 0.834171 | 83.155% |
| 1 | 0 | 155209.5 | 15.830% | 1.849019 | 66.460% | 0.047589 | 0.563904 | 0.233850 | 0.762036 | 73.272% |
| 2 | 0 | 166951.7 | 24.593% | 1.672296 | 69.666% | 0.041341 | 0.540897 | 0.251726 | 0.747897 | 70.953% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
