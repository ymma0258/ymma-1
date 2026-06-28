# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 13.225320 | 0.000% | 0.296213 | 3.638935 | 0.149829 | 0.842488 | 88.028% |
| 1 | 0 | 162079.7 | 20.957% | 5.483323 | 58.539% | 0.082457 | 1.973870 | 0.264337 | 0.764401 | 76.553% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
