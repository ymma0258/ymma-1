# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.190006 | 0.000% | 0.239074 | 2.708218 | 0.216232 | 0.867744 | 88.988% |
| 1 | 0 | 181582.2 | 23.752% | 3.723314 | 54.538% | 0.083282 | 1.505130 | 0.345243 | 0.816934 | 80.313% |
| 1 | 1 | 197045.3 | 34.290% | 2.973837 | 63.689% | 0.060553 | 1.226287 | 0.334821 | 0.783805 | 75.060% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
