# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 6.211368 | 0.000% | 0.199894 | 1.886772 | 0.225351 | 0.860322 | 86.816% |
| 0.25 | 0 | 141245.0 | 5.303% | 4.388726 | 29.344% | 0.132956 | 1.415793 | 0.235737 | 0.841978 | 83.139% |
| 0.5 | 0 | 145847.1 | 8.734% | 3.407800 | 45.136% | 0.089758 | 1.265139 | 0.275712 | 0.818667 | 79.418% |
| 1 | 0 | 153486.8 | 14.430% | 2.791568 | 55.057% | 0.060583 | 1.054497 | 0.285403 | 0.787020 | 74.995% |
| 2 | 0 | 164847.2 | 22.900% | 1.778903 | 71.361% | 0.032372 | 0.547673 | 0.199098 | 0.696928 | 62.314% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
