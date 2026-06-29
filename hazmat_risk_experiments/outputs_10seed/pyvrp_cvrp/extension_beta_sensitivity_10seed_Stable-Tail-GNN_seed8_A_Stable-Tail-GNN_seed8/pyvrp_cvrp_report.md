# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.634359 | 0.000% | 0.229405 | 2.385096 | 0.166464 | 0.885783 | 90.393% |
| 0.5 | 0 | 148768.7 | 11.023% | 4.103556 | 46.249% | 0.109749 | 1.685447 | 0.321050 | 0.857770 | 85.368% |
| 1 | 0 | 157997.4 | 17.911% | 3.011525 | 60.553% | 0.074084 | 0.869025 | 0.199251 | 0.822900 | 80.016% |
| 1.5 | 0 | 165706.7 | 23.664% | 2.477554 | 67.547% | 0.053408 | 0.850876 | 0.288426 | 0.802091 | 76.014% |
| 2 | 0 | 172268.9 | 28.561% | 2.248659 | 70.546% | 0.047475 | 0.876601 | 0.325153 | 0.787648 | 73.771% |
| 3 | 0 | 184012.6 | 37.325% | 2.087774 | 72.653% | 0.042226 | 0.867415 | 0.307827 | 0.768328 | 70.942% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
