# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 9.101238 | 0.000% | 0.283889 | 2.835823 | 0.203504 | 0.871292 | 90.038% |
| 0.25 | 0 | 158335.5 | 7.616% | 8.019057 | 11.890% | 0.215172 | 2.488375 | 0.210170 | 0.870937 | 89.749% |
| 0.5 | 0 | 168202.8 | 14.322% | 5.617683 | 38.276% | 0.164599 | 1.823489 | 0.225830 | 0.857015 | 86.307% |
| 1 | 0 | 179750.3 | 22.171% | 3.848752 | 57.712% | 0.096255 | 1.325685 | 0.281295 | 0.820433 | 80.548% |
| 2 | 0 | 197656.9 | 34.341% | 3.148319 | 65.408% | 0.063135 | 0.963028 | 0.243257 | 0.796265 | 76.512% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
