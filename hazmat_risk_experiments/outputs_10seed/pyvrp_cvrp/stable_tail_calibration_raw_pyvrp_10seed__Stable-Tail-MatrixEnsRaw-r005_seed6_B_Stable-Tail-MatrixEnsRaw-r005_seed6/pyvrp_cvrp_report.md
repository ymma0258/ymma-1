# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 8.401573 | 0.000% | 0.248783 | 2.907276 | 0.239583 | 0.868843 | 89.261% |
| 0.25 | 0 | 157868.6 | 7.201% | 7.366365 | 12.322% | 0.186820 | 2.425401 | 0.228500 | 0.867924 | 89.169% |
| 0.5 | 0 | 168349.2 | 14.318% | 5.860489 | 30.245% | 0.147966 | 1.715067 | 0.196257 | 0.857743 | 86.657% |
| 1 | 0 | 181295.6 | 23.109% | 3.984016 | 52.580% | 0.098743 | 1.471035 | 0.317875 | 0.826831 | 81.260% |
| 2 | 0 | 202450.7 | 37.475% | 3.502830 | 58.307% | 0.088285 | 1.298737 | 0.339465 | 0.815474 | 78.903% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
