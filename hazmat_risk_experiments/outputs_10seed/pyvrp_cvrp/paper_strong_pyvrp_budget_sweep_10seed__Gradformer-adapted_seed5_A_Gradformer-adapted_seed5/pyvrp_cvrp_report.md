# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.5 | 0.000% | 8.778411 | 0.000% | 0.272042 | 2.643145 | 0.170322 | 0.857060 | 88.220% |
| 0.25 | 0 | 142079.9 | 5.768% | 6.663775 | 24.089% | 0.208135 | 2.135766 | 0.219661 | 0.855901 | 87.950% |
| 0.5 | 0 | 148871.6 | 10.824% | 5.159955 | 41.220% | 0.138619 | 1.648249 | 0.235073 | 0.838193 | 84.928% |
| 1 | 0 | 156745.9 | 16.686% | 3.490377 | 60.239% | 0.076537 | 1.245048 | 0.282228 | 0.786623 | 77.670% |
| 2 | 0 | 170070.4 | 26.605% | 2.958959 | 66.293% | 0.062794 | 0.984532 | 0.272823 | 0.765066 | 74.350% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
