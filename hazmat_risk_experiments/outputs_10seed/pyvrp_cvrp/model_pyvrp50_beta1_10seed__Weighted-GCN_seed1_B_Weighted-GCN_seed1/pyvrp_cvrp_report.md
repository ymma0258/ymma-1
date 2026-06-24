# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.820255 | 0.000% | 0.274643 | 2.734975 | 0.183482 | 0.840115 | 87.333% |
| 1 | 0 | 175808.8 | 19.817% | 3.886008 | 55.942% | 0.074117 | 1.132707 | 0.198946 | 0.730907 | 73.195% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
