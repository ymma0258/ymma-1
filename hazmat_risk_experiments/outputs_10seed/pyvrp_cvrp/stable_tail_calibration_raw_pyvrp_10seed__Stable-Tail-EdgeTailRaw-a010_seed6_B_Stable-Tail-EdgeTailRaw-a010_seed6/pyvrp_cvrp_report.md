# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 9.266258 | 0.000% | 0.281608 | 3.053942 | 0.226720 | 0.872301 | 89.626% |
| 0.25 | 0 | 157869.4 | 7.299% | 8.019525 | 13.455% | 0.200478 | 2.551237 | 0.218519 | 0.869444 | 89.340% |
| 0.5 | 0 | 168366.0 | 14.433% | 6.364395 | 31.316% | 0.157853 | 2.402670 | 0.290589 | 0.860062 | 87.084% |
| 1 | 0 | 181433.6 | 23.315% | 4.372476 | 52.813% | 0.111495 | 1.751715 | 0.352450 | 0.832281 | 82.127% |
| 2 | 0 | 202397.6 | 37.563% | 3.746700 | 59.566% | 0.095888 | 1.497227 | 0.348327 | 0.817527 | 79.231% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
