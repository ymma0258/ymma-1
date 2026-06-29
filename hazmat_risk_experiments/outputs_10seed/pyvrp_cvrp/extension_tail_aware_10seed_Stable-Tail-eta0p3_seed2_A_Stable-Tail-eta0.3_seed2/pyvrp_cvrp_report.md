# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 10.623048 | 0.000% | 0.241295 | 3.120930 | 0.159331 | 0.877150 | 90.246% |
| 1 | 0 | 157648.8 | 17.651% | 4.204841 | 60.418% | 0.076304 | 1.326206 | 0.263482 | 0.826382 | 80.116% |
| 2 | 0 | 171864.9 | 28.260% | 3.698623 | 65.183% | 0.069122 | 1.326710 | 0.332975 | 0.808803 | 77.266% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
