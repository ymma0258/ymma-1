# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.304075 | 0.000% | 0.200452 | 2.465942 | 0.225098 | 0.852842 | 87.728% |
| 1 | 0 | 177088.3 | 20.689% | 3.408170 | 53.339% | 0.086586 | 1.265918 | 0.329832 | 0.786691 | 78.067% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
