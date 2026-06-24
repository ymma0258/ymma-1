# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.363411 | 0.000% | 0.293597 | 3.146112 | 0.229273 | 0.860843 | 89.646% |
| 1 | 0 | 181883.0 | 23.957% | 5.034890 | 46.228% | 0.139932 | 1.655076 | 0.252557 | 0.830082 | 83.332% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
