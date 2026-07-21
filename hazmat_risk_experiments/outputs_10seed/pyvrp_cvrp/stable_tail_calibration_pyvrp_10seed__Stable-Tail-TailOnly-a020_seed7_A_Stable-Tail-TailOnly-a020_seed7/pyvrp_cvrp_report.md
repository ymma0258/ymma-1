# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 9.261608 | 0.000% | 0.305974 | 2.652309 | 0.169783 | 0.875226 | 89.794% |
| 0.25 | 0 | 143134.3 | 6.818% | 6.067039 | 34.493% | 0.179152 | 1.883115 | 0.232450 | 0.861103 | 87.067% |
| 0.5 | 0 | 149257.4 | 11.388% | 4.602068 | 50.310% | 0.132207 | 1.724938 | 0.269889 | 0.836256 | 83.294% |
| 1 | 0 | 158361.3 | 18.182% | 3.280148 | 64.583% | 0.087863 | 1.199824 | 0.284540 | 0.800476 | 77.454% |
| 2 | 0 | 171552.0 | 28.026% | 2.614882 | 71.766% | 0.062720 | 0.859684 | 0.255181 | 0.766212 | 72.055% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
