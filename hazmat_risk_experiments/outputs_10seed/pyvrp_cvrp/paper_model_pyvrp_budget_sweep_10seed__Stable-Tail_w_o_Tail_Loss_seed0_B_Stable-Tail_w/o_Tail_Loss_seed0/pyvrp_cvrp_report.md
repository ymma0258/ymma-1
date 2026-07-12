# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.6 | 0.000% | 7.284263 | 0.000% | 0.228788 | 2.469206 | 0.239277 | 0.875309 | 90.000% |
| 0.25 | 0 | 156609.2 | 6.298% | 6.630598 | 8.974% | 0.199053 | 2.290684 | 0.211184 | 0.875739 | 89.632% |
| 0.5 | 0 | 165291.3 | 12.191% | 4.827569 | 33.726% | 0.136776 | 1.756204 | 0.266486 | 0.865143 | 86.773% |
| 1 | 0 | 176499.4 | 19.798% | 3.491273 | 52.071% | 0.079367 | 1.292500 | 0.304409 | 0.838443 | 82.433% |
| 2 | 0 | 193871.0 | 31.589% | 2.737543 | 62.418% | 0.056907 | 1.037091 | 0.335906 | 0.818725 | 78.246% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
