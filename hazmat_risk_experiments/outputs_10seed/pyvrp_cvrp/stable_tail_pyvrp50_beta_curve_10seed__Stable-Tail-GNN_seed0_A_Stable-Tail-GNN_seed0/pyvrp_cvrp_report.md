# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.397525 | 0.000% | 0.232973 | 2.390638 | 0.223678 | 0.880360 | 90.067% |
| 0.25 | 0 | 142859.3 | 6.613% | 5.164632 | 30.184% | 0.150269 | 1.536152 | 0.170765 | 0.868812 | 87.569% |
| 0.5 | 0 | 148738.8 | 11.001% | 3.992004 | 46.036% | 0.122844 | 2.081000 | 0.391020 | 0.842903 | 84.461% |
| 1 | 0 | 156818.2 | 17.031% | 2.407933 | 67.449% | 0.052249 | 0.874088 | 0.254022 | 0.789544 | 75.383% |
| 2 | 0 | 167975.9 | 25.357% | 1.667111 | 77.464% | 0.030881 | 0.468700 | 0.186878 | 0.710219 | 63.995% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
