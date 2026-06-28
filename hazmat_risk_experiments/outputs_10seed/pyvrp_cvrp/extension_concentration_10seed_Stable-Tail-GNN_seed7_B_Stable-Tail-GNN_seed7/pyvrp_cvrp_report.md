# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.851676 | 0.000% | 0.287040 | 3.185509 | 0.204509 | 0.879458 | 90.687% |
| 1 | 0 | 177190.3 | 20.759% | 3.710676 | 62.335% | 0.080461 | 1.295202 | 0.270191 | 0.820447 | 78.846% |
| 1 | 0.5 | 183764.3 | 25.239% | 3.311894 | 66.382% | 0.071342 | 1.017634 | 0.249187 | 0.810304 | 76.871% |
| 1 | 1 | 189951.6 | 29.456% | 3.238929 | 67.123% | 0.068575 | 1.027958 | 0.251002 | 0.806733 | 76.248% |
| 1 | 2 | 201515.9 | 37.337% | 3.018053 | 69.365% | 0.065196 | 1.146594 | 0.355905 | 0.798382 | 74.369% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
