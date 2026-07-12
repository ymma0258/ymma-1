# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.1 | 0.000% | 7.462531 | 0.000% | 0.222338 | 2.183712 | 0.175464 | 0.873885 | 86.936% |
| 0.25 | 0 | 155771.8 | 5.921% | 6.300139 | 15.576% | 0.179361 | 1.914530 | 0.217862 | 0.864375 | 84.951% |
| 0.5 | 0 | 163234.2 | 10.995% | 4.566639 | 38.806% | 0.123569 | 1.739418 | 0.303639 | 0.833264 | 79.723% |
| 1 | 0 | 172690.8 | 17.426% | 3.021007 | 59.518% | 0.066676 | 1.411263 | 0.340727 | 0.776657 | 70.648% |
| 2 | 0 | 187616.4 | 27.575% | 2.662839 | 64.317% | 0.051183 | 1.416954 | 0.383596 | 0.759745 | 67.871% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
