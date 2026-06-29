# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.072629 | 0.000% | 0.224033 | 2.220910 | 0.199043 | 0.877152 | 89.589% |
| 1 | 0 | 154376.7 | 15.209% | 2.271279 | 67.886% | 0.046362 | 0.709523 | 0.180468 | 0.758245 | 72.274% |
| 1 | 0.5 | 158472.0 | 18.265% | 2.299212 | 67.491% | 0.049253 | 0.798538 | 0.240537 | 0.771653 | 73.713% |
| 1 | 1 | 162191.6 | 21.041% | 1.952961 | 72.387% | 0.036711 | 0.560344 | 0.193877 | 0.741890 | 69.365% |
| 1 | 2 | 169032.9 | 26.146% | 1.802190 | 74.519% | 0.033592 | 0.520593 | 0.198431 | 0.721352 | 66.398% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
