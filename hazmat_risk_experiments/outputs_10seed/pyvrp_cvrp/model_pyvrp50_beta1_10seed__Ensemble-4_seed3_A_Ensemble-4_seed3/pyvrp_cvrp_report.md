# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.435602 | 0.000% | 0.210126 | 2.329849 | 0.188730 | 0.847940 | 87.491% |
| 1 | 0 | 157996.8 | 17.910% | 2.961443 | 60.172% | 0.066138 | 0.903583 | 0.201660 | 0.735738 | 73.351% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
