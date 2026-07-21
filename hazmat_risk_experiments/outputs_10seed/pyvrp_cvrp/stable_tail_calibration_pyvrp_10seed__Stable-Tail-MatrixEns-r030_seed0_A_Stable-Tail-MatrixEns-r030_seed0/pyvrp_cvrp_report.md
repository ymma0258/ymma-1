# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 5.504528 | 0.000% | 0.163480 | 1.716782 | 0.212537 | 0.884738 | 90.482% |
| 0.25 | 0 | 142281.2 | 6.182% | 3.372173 | 38.738% | 0.102865 | 1.167291 | 0.258327 | 0.866047 | 86.965% |
| 0.5 | 0 | 148041.0 | 10.480% | 2.682040 | 51.276% | 0.080121 | 1.136514 | 0.309442 | 0.845764 | 84.152% |
| 1 | 0 | 155592.8 | 16.116% | 1.700221 | 69.112% | 0.039595 | 0.651126 | 0.284677 | 0.783335 | 74.932% |
| 2 | 0 | 167421.6 | 24.943% | 1.308232 | 76.234% | 0.024277 | 0.413396 | 0.221805 | 0.739704 | 67.996% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
