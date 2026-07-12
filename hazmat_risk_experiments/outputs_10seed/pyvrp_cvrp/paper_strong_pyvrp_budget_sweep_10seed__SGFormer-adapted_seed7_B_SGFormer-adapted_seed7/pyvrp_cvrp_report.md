# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.9 | 0.000% | 8.339759 | 0.000% | 0.252069 | 2.565202 | 0.206906 | 0.877297 | 88.202% |
| 0.25 | 0 | 157731.9 | 7.060% | 6.890169 | 17.382% | 0.206994 | 2.340041 | 0.271549 | 0.864885 | 86.445% |
| 0.5 | 0 | 165760.6 | 12.509% | 3.982519 | 52.247% | 0.087560 | 1.268529 | 0.231358 | 0.810269 | 77.638% |
| 1 | 0 | 175451.3 | 19.087% | 3.172209 | 61.963% | 0.062534 | 1.078498 | 0.267490 | 0.789939 | 73.231% |
| 2 | 0 | 192364.0 | 30.566% | 2.652184 | 68.198% | 0.050889 | 0.905304 | 0.264889 | 0.765137 | 68.881% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
