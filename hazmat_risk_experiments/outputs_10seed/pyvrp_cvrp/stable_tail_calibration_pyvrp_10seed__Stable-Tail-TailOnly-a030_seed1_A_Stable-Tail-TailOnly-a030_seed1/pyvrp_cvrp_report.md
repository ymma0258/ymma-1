# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.2 | 0.000% | 9.297843 | 0.000% | 0.301370 | 2.534940 | 0.135961 | 0.874440 | 90.026% |
| 0.25 | 0 | 141467.5 | 5.574% | 6.594785 | 29.072% | 0.201347 | 1.923003 | 0.184988 | 0.867996 | 88.229% |
| 0.5 | 0 | 147123.2 | 9.795% | 4.647913 | 50.011% | 0.120136 | 1.432387 | 0.209299 | 0.845097 | 84.132% |
| 1 | 0 | 155080.9 | 15.734% | 3.298887 | 64.520% | 0.080795 | 1.033001 | 0.203208 | 0.796719 | 77.409% |
| 2 | 0 | 166754.6 | 24.445% | 2.767473 | 70.235% | 0.059310 | 0.917149 | 0.265638 | 0.774553 | 73.810% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
