# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.9 | 0.000% | 7.621270 | 0.000% | 0.235506 | 2.179518 | 0.150597 | 0.864592 | 88.313% |
| 0.25 | 0 | 142519.2 | 6.359% | 5.585813 | 26.708% | 0.151688 | 1.801499 | 0.223643 | 0.849747 | 86.306% |
| 0.5 | 0 | 148306.5 | 10.678% | 4.052283 | 46.829% | 0.111448 | 1.567422 | 0.277773 | 0.821729 | 82.346% |
| 1 | 0 | 156922.2 | 17.108% | 2.771326 | 63.637% | 0.072272 | 0.907870 | 0.231392 | 0.765982 | 74.290% |
| 2 | 0 | 169514.6 | 26.505% | 2.325105 | 69.492% | 0.051967 | 0.756911 | 0.238118 | 0.736203 | 69.953% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
