# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 8.563605 | 0.000% | 0.277054 | 2.551150 | 0.181119 | 0.875658 | 89.455% |
| 0.25 | 0 | 142314.3 | 6.206% | 5.954087 | 30.472% | 0.173309 | 2.005403 | 0.247870 | 0.865229 | 87.740% |
| 0.5 | 0 | 148457.6 | 10.791% | 4.700051 | 45.116% | 0.140822 | 1.668506 | 0.261601 | 0.852304 | 85.143% |
| 1 | 0 | 157429.7 | 17.487% | 3.282038 | 61.675% | 0.074082 | 1.213160 | 0.319738 | 0.809802 | 78.824% |
| 2 | 0 | 171759.3 | 28.180% | 2.854485 | 66.667% | 0.063696 | 1.168326 | 0.347014 | 0.792030 | 75.868% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
