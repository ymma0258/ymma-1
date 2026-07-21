# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.4 | 0.000% | 6.885415 | 0.000% | 0.198917 | 2.389425 | 0.254530 | 0.868797 | 88.810% |
| 0.25 | 0 | 155507.6 | 5.646% | 5.749991 | 16.490% | 0.140428 | 2.185269 | 0.289509 | 0.864762 | 87.839% |
| 0.5 | 0 | 163572.2 | 11.124% | 4.585121 | 33.408% | 0.116746 | 1.911831 | 0.301282 | 0.851882 | 85.502% |
| 1 | 0 | 175503.9 | 19.230% | 3.604053 | 47.657% | 0.091640 | 1.352520 | 0.285675 | 0.834174 | 82.082% |
| 2 | 0 | 192215.1 | 30.583% | 2.670051 | 61.222% | 0.066136 | 1.191939 | 0.331532 | 0.806701 | 77.073% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
