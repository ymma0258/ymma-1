# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 9.386124 | 0.000% | 0.276187 | 2.839348 | 0.180017 | 0.865650 | 89.931% |
| 0.25 | 0 | 157202.0 | 7.039% | 7.704788 | 17.913% | 0.224680 | 2.361150 | 0.193734 | 0.862598 | 89.088% |
| 0.5 | 0 | 166740.6 | 13.534% | 6.412789 | 31.678% | 0.181655 | 2.109973 | 0.226967 | 0.853913 | 87.104% |
| 1 | 0 | 179915.2 | 22.505% | 4.266553 | 54.544% | 0.098223 | 1.428546 | 0.262106 | 0.824497 | 81.716% |
| 2 | 0 | 198438.1 | 35.117% | 3.506782 | 62.639% | 0.076013 | 1.175814 | 0.256153 | 0.800717 | 77.741% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
