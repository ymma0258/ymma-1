# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 8.711858 | 0.000% | 0.270993 | 2.455719 | 0.166411 | 0.877727 | 90.067% |
| 0.25 | 0 | 143465.9 | 6.800% | 6.105475 | 29.918% | 0.190389 | 1.939758 | 0.228823 | 0.867306 | 87.926% |
| 0.5 | 0 | 150165.4 | 11.787% | 4.915729 | 43.574% | 0.151342 | 1.656061 | 0.258448 | 0.852577 | 85.554% |
| 1 | 0 | 159969.8 | 19.086% | 3.523192 | 59.559% | 0.096260 | 1.160899 | 0.278335 | 0.814747 | 79.881% |
| 2 | 0 | 175286.5 | 30.488% | 2.850303 | 67.282% | 0.067311 | 1.046738 | 0.328701 | 0.786448 | 75.572% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
