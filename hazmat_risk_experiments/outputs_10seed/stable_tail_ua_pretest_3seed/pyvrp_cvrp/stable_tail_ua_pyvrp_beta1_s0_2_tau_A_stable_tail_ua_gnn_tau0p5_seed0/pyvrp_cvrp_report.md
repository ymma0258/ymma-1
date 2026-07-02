# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 13.043068 | 0.000% | 0.332890 | 3.523839 | 0.142424 | 0.836390 | 87.296% |
| 1 | 0 | 162869.7 | 21.547% | 5.865199 | 55.032% | 0.123085 | 2.037314 | 0.228615 | 0.766651 | 77.080% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
