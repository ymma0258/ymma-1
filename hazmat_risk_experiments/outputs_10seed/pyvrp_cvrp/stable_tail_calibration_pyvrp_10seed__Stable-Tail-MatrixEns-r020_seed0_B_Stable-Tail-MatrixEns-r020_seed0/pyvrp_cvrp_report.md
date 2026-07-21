# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 5.983726 | 0.000% | 0.163525 | 2.025856 | 0.249187 | 0.877525 | 89.383% |
| 0.25 | 0 | 156445.5 | 6.524% | 5.011163 | 16.253% | 0.121161 | 1.758274 | 0.250102 | 0.869643 | 88.127% |
| 0.5 | 0 | 165066.9 | 12.394% | 3.637749 | 39.206% | 0.091916 | 1.271449 | 0.243349 | 0.849501 | 84.256% |
| 1 | 0 | 175250.5 | 19.329% | 2.524920 | 57.804% | 0.062587 | 0.991149 | 0.315639 | 0.816487 | 78.912% |
| 2 | 0 | 190190.6 | 29.501% | 1.909474 | 68.089% | 0.038829 | 0.694883 | 0.278940 | 0.775734 | 72.102% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
