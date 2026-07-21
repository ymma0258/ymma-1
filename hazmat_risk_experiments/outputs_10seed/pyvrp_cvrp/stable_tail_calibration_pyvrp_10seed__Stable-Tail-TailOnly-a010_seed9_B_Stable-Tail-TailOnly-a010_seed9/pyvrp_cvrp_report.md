# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.124242 | 0.000% | 0.288698 | 2.894685 | 0.215238 | 0.872545 | 90.124% |
| 0.25 | 0 | 157981.6 | 7.472% | 7.804721 | 14.462% | 0.220190 | 2.552027 | 0.221109 | 0.870562 | 89.634% |
| 0.5 | 0 | 167740.4 | 14.111% | 5.101782 | 44.085% | 0.135925 | 1.581850 | 0.240989 | 0.845627 | 84.962% |
| 1 | 0 | 178960.7 | 21.744% | 3.384660 | 62.905% | 0.076497 | 1.095371 | 0.253638 | 0.806115 | 78.600% |
| 2 | 0 | 196016.6 | 33.347% | 3.049586 | 66.577% | 0.059691 | 0.954158 | 0.237041 | 0.792988 | 76.438% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
