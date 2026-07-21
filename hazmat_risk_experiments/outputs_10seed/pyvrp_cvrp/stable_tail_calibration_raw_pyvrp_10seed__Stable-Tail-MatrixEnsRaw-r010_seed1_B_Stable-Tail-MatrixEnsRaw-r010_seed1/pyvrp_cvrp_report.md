# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.9 | 0.000% | 8.756199 | 0.000% | 0.276482 | 2.973302 | 0.254164 | 0.872903 | 89.884% |
| 0.25 | 0 | 156003.4 | 6.175% | 7.368190 | 15.852% | 0.214032 | 2.460145 | 0.248488 | 0.870922 | 89.047% |
| 0.5 | 0 | 163854.2 | 11.518% | 6.084165 | 30.516% | 0.155558 | 1.948157 | 0.252328 | 0.862486 | 87.094% |
| 1 | 0 | 173762.0 | 18.261% | 3.465128 | 60.427% | 0.079438 | 1.164042 | 0.240069 | 0.811011 | 78.683% |
| 2 | 0 | 187893.8 | 27.879% | 2.978967 | 65.979% | 0.059129 | 1.045164 | 0.265158 | 0.799262 | 76.335% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
