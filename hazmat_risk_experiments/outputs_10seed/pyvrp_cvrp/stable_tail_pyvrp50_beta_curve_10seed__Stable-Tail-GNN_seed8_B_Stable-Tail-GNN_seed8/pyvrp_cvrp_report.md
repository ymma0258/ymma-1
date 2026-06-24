# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.420933 | 0.000% | 0.217788 | 2.362199 | 0.193787 | 0.878179 | 89.055% |
| 0.25 | 0 | 155839.0 | 6.207% | 6.291340 | 15.222% | 0.151407 | 2.220765 | 0.227028 | 0.873246 | 88.242% |
| 0.5 | 0 | 164480.2 | 12.096% | 4.636871 | 37.516% | 0.118479 | 1.675302 | 0.288291 | 0.848277 | 84.356% |
| 1 | 0 | 175079.5 | 19.320% | 3.158386 | 57.440% | 0.081404 | 1.260882 | 0.325850 | 0.815500 | 78.509% |
| 2 | 0 | 190834.4 | 30.057% | 2.465958 | 66.770% | 0.051741 | 0.937488 | 0.299515 | 0.786869 | 73.552% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
