# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.9 | 0.000% | 8.300410 | 0.000% | 0.267446 | 2.548653 | 0.203150 | 0.879274 | 89.205% |
| 0.25 | 0 | 142905.9 | 6.595% | 5.280811 | 36.379% | 0.141395 | 1.898108 | 0.278811 | 0.864703 | 85.780% |
| 0.5 | 0 | 148852.4 | 11.030% | 4.249516 | 48.804% | 0.114294 | 1.473410 | 0.259789 | 0.845077 | 82.757% |
| 1 | 0 | 157072.2 | 17.161% | 2.847604 | 65.693% | 0.067537 | 1.104969 | 0.270469 | 0.795671 | 75.011% |
| 2 | 0 | 168234.9 | 25.488% | 2.110638 | 74.572% | 0.036878 | 0.593108 | 0.206344 | 0.745332 | 67.545% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
