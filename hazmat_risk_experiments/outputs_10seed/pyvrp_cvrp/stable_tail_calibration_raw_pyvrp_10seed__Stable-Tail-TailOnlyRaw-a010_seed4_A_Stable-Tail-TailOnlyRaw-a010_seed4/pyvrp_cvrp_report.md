# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 9.326993 | 0.000% | 0.296138 | 2.812730 | 0.190923 | 0.880840 | 90.437% |
| 0.25 | 0 | 143557.6 | 6.921% | 6.942339 | 25.567% | 0.214254 | 2.127148 | 0.213339 | 0.876260 | 89.296% |
| 0.5 | 0 | 150367.8 | 11.993% | 4.975694 | 46.653% | 0.150406 | 1.490862 | 0.223988 | 0.852854 | 85.476% |
| 1 | 0 | 160247.1 | 19.352% | 3.723104 | 60.082% | 0.101957 | 1.247171 | 0.276487 | 0.827281 | 81.356% |
| 2 | 0 | 175237.1 | 30.516% | 2.869387 | 69.236% | 0.070473 | 1.131557 | 0.390300 | 0.792325 | 76.140% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
