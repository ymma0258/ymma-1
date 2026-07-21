# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 4.455821 | 0.000% | 0.136483 | 1.303770 | 0.168539 | 0.874198 | 89.004% |
| 0.25 | 0 | 142242.1 | 6.152% | 3.194015 | 28.318% | 0.090597 | 0.987543 | 0.225173 | 0.862803 | 86.836% |
| 0.5 | 0 | 147701.0 | 10.226% | 2.260026 | 49.279% | 0.066417 | 0.918863 | 0.326665 | 0.830724 | 82.232% |
| 1 | 0 | 155807.8 | 16.276% | 1.523045 | 65.819% | 0.039471 | 0.588005 | 0.274084 | 0.770996 | 73.731% |
| 2 | 0 | 166902.7 | 24.556% | 1.117033 | 74.931% | 0.024143 | 0.368037 | 0.249312 | 0.714814 | 65.257% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
