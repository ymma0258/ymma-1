# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 8.528879 | 0.000% | 0.257869 | 2.709720 | 0.208774 | 0.874049 | 89.188% |
| 0.25 | 0 | 156327.9 | 6.203% | 7.399308 | 13.244% | 0.210829 | 2.317099 | 0.210934 | 0.872538 | 88.532% |
| 0.5 | 0 | 165050.2 | 12.129% | 5.745854 | 32.631% | 0.154117 | 1.998466 | 0.275159 | 0.855225 | 85.513% |
| 1 | 0 | 175445.1 | 19.190% | 3.931408 | 53.905% | 0.098135 | 1.557023 | 0.311411 | 0.819848 | 80.087% |
| 2 | 0 | 191433.3 | 30.052% | 3.059138 | 64.132% | 0.061227 | 1.255640 | 0.333527 | 0.795011 | 76.036% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
