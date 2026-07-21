# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 5.163364 | 0.000% | 0.157268 | 1.626863 | 0.197165 | 0.874216 | 89.240% |
| 0.25 | 0 | 155936.2 | 6.177% | 4.448408 | 13.847% | 0.129700 | 1.537845 | 0.233471 | 0.871493 | 88.516% |
| 0.5 | 0 | 164589.7 | 12.070% | 3.317686 | 35.746% | 0.086418 | 0.998316 | 0.229902 | 0.853902 | 85.211% |
| 1 | 0 | 174880.8 | 19.077% | 2.353536 | 54.419% | 0.061115 | 0.967456 | 0.340077 | 0.821653 | 80.176% |
| 2 | 0 | 191363.0 | 30.300% | 1.929141 | 62.638% | 0.039975 | 0.750946 | 0.304697 | 0.800249 | 76.883% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
