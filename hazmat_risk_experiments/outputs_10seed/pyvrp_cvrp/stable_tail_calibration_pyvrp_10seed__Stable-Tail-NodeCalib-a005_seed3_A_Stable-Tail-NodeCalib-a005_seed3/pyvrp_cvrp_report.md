# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 7.046078 | 0.000% | 0.211703 | 2.296920 | 0.193800 | 0.872114 | 88.746% |
| 0.25 | 0 | 141841.0 | 5.748% | 4.900587 | 30.449% | 0.145061 | 1.482920 | 0.192992 | 0.858511 | 86.897% |
| 0.5 | 0 | 147487.8 | 9.958% | 3.688597 | 47.650% | 0.108133 | 1.207260 | 0.217665 | 0.834277 | 83.286% |
| 1 | 0 | 155735.1 | 16.106% | 2.517864 | 64.266% | 0.066827 | 0.756261 | 0.214007 | 0.776507 | 75.461% |
| 2 | 0 | 168146.2 | 25.359% | 2.169275 | 69.213% | 0.052435 | 0.680111 | 0.245152 | 0.753984 | 71.886% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
