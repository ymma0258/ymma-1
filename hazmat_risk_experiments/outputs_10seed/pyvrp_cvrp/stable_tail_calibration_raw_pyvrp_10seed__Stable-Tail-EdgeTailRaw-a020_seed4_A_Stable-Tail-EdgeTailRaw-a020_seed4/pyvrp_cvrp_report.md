# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.4 | 0.000% | 9.522045 | 0.000% | 0.305375 | 2.650394 | 0.152904 | 0.879855 | 90.245% |
| 0.25 | 0 | 143318.7 | 6.585% | 5.909791 | 37.936% | 0.181404 | 1.806122 | 0.227459 | 0.864017 | 87.371% |
| 0.5 | 0 | 150165.6 | 11.677% | 5.026573 | 47.211% | 0.152551 | 1.630337 | 0.246029 | 0.855506 | 85.776% |
| 1 | 0 | 159659.5 | 18.737% | 3.688766 | 61.261% | 0.092943 | 1.288864 | 0.291036 | 0.821978 | 80.820% |
| 2 | 0 | 174466.8 | 29.749% | 2.960779 | 68.906% | 0.070773 | 1.096753 | 0.345398 | 0.795060 | 76.689% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
