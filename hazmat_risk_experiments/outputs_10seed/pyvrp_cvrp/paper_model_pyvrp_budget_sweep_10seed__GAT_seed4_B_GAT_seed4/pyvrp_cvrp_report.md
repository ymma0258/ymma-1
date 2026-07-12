# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.5 | 0.000% | 7.446122 | 0.000% | 0.220297 | 2.780164 | 0.272586 | 0.861717 | 88.200% |
| 0.25 | 0 | 155428.7 | 5.497% | 6.388597 | 14.202% | 0.183828 | 1.922805 | 0.200886 | 0.858771 | 87.277% |
| 0.5 | 0 | 164235.1 | 11.474% | 5.542785 | 25.561% | 0.144507 | 1.909525 | 0.243164 | 0.851994 | 85.682% |
| 1 | 0 | 176796.3 | 20.000% | 4.445385 | 40.299% | 0.119830 | 1.651331 | 0.316952 | 0.833141 | 82.445% |
| 2 | 0 | 198222.4 | 34.543% | 3.999465 | 46.288% | 0.093368 | 1.749832 | 0.365668 | 0.828354 | 81.199% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
