# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 5.337926 | 0.000% | 0.173410 | 1.544384 | 0.167985 | 0.873267 | 89.408% |
| 0.25 | 0 | 142916.4 | 6.656% | 3.700734 | 30.671% | 0.110324 | 1.205201 | 0.221724 | 0.861906 | 87.111% |
| 0.5 | 0 | 149119.8 | 11.285% | 2.728739 | 48.880% | 0.079187 | 0.921976 | 0.213232 | 0.839022 | 83.371% |
| 1 | 0 | 158193.8 | 18.057% | 1.966887 | 63.153% | 0.053552 | 0.735252 | 0.303352 | 0.800184 | 77.417% |
| 2 | 0 | 170867.6 | 27.515% | 1.567310 | 70.638% | 0.038118 | 0.496009 | 0.247385 | 0.766866 | 72.120% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
