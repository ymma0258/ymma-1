# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.1 | 0.000% | 8.427566 | 0.000% | 0.271271 | 2.576584 | 0.184305 | 0.866586 | 88.843% |
| 0.25 | 0 | 143327.1 | 6.644% | 5.818631 | 30.957% | 0.163266 | 1.848494 | 0.203764 | 0.856845 | 87.362% |
| 0.5 | 0 | 149746.2 | 11.420% | 4.440409 | 47.311% | 0.121399 | 1.692706 | 0.264042 | 0.830299 | 83.786% |
| 1 | 0 | 159110.8 | 18.388% | 3.012734 | 64.251% | 0.071548 | 1.011101 | 0.250234 | 0.777097 | 76.287% |
| 2 | 0 | 173187.2 | 28.861% | 2.310841 | 72.580% | 0.046948 | 0.708390 | 0.217976 | 0.730165 | 69.632% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
