# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147396.9 | 0.000% | 5.204090 | 0.000% | 0.136091 | 1.736236 | 0.229553 | 0.840343 | 82.166% |
| 0.25 | 0 | 152878.8 | 3.719% | 3.878809 | 25.466% | 0.086966 | 1.560451 | 0.271950 | 0.818364 | 77.913% |
| 0.5 | 0 | 158094.0 | 7.257% | 2.772285 | 46.729% | 0.059079 | 0.958660 | 0.236588 | 0.765177 | 69.393% |
| 1 | 0 | 165048.5 | 11.976% | 2.114491 | 59.369% | 0.038489 | 0.579789 | 0.141967 | 0.706692 | 61.695% |
| 2 | 0 | 176804.4 | 19.951% | 1.873332 | 64.003% | 0.032412 | 0.543383 | 0.162611 | 0.687402 | 58.008% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
