# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 7.565139 | 0.000% | 0.220631 | 2.275979 | 0.189676 | 0.860547 | 87.809% |
| 0.25 | 0 | 156650.6 | 6.374% | 6.308751 | 16.608% | 0.157258 | 2.109668 | 0.233003 | 0.853502 | 86.634% |
| 0.5 | 0 | 165044.4 | 12.074% | 4.709190 | 37.751% | 0.114023 | 1.456003 | 0.218210 | 0.834230 | 83.247% |
| 1 | 0 | 176924.2 | 20.141% | 3.243892 | 57.121% | 0.076290 | 1.169839 | 0.248471 | 0.788190 | 76.555% |
| 2 | 0 | 191225.3 | 29.852% | 2.427128 | 67.917% | 0.051350 | 0.759080 | 0.229100 | 0.751186 | 70.313% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
