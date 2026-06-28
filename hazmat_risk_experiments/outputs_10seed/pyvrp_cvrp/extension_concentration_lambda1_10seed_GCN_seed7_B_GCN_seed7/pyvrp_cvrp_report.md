# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.442787 | 0.000% | 0.293933 | 3.399195 | 0.220726 | 0.856399 | 89.822% |
| 1 | 0 | 180829.8 | 23.239% | 5.358001 | 48.692% | 0.150843 | 1.668325 | 0.215687 | 0.819740 | 83.095% |
| 1 | 1 | 199032.2 | 35.644% | 4.072538 | 61.001% | 0.097494 | 1.455999 | 0.338658 | 0.787010 | 77.462% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
