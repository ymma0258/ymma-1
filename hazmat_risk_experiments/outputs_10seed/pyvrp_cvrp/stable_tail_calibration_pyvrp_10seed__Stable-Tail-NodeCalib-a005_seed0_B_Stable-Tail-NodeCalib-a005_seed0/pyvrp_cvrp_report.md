# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147396.9 | 0.000% | 7.663213 | 0.000% | 0.216991 | 2.545468 | 0.253920 | 0.877486 | 89.518% |
| 0.25 | 0 | 156889.6 | 6.440% | 6.469691 | 15.575% | 0.160315 | 2.355674 | 0.268940 | 0.872997 | 88.336% |
| 0.5 | 0 | 165372.9 | 12.196% | 4.549066 | 40.638% | 0.114934 | 1.504795 | 0.226363 | 0.850053 | 84.374% |
| 1 | 0 | 176531.6 | 19.766% | 3.067031 | 59.977% | 0.074527 | 1.163760 | 0.306967 | 0.812515 | 78.107% |
| 2 | 0 | 191543.1 | 29.951% | 2.395060 | 68.746% | 0.051268 | 0.895818 | 0.272087 | 0.775095 | 71.926% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
