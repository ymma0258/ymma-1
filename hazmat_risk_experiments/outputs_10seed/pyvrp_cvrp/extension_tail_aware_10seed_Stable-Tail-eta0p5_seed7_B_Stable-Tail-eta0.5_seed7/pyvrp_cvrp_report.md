# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 13.146276 | 0.000% | 0.249912 | 4.224433 | 0.197162 | 0.880777 | 90.874% |
| 1 | 0 | 178048.0 | 21.343% | 5.008218 | 61.904% | 0.063617 | 1.627561 | 0.235838 | 0.828793 | 79.484% |
| 2 | 0 | 195009.1 | 32.903% | 4.556178 | 65.342% | 0.058334 | 1.355160 | 0.216959 | 0.817252 | 77.676% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
