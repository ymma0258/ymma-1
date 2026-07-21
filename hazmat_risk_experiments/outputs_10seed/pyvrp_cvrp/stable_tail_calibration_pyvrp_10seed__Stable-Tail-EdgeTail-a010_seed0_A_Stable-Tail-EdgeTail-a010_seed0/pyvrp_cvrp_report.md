# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 7.779003 | 0.000% | 0.238957 | 2.622848 | 0.230156 | 0.884228 | 90.151% |
| 0.25 | 0 | 142779.0 | 6.394% | 4.693369 | 39.666% | 0.138025 | 1.736038 | 0.257126 | 0.859888 | 86.266% |
| 0.5 | 0 | 148521.5 | 10.673% | 3.629360 | 53.344% | 0.106454 | 1.277142 | 0.271006 | 0.836481 | 82.780% |
| 1 | 0 | 156295.3 | 16.466% | 2.438152 | 68.657% | 0.059719 | 0.923095 | 0.256325 | 0.782761 | 74.995% |
| 2 | 0 | 168243.8 | 25.370% | 1.773208 | 77.205% | 0.031192 | 0.557289 | 0.227093 | 0.722336 | 65.758% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
