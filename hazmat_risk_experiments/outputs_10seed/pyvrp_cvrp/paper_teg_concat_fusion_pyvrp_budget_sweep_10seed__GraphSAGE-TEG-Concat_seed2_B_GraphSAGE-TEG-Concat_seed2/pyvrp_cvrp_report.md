# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.5 | 0.000% | 8.845039 | 0.000% | 0.271997 | 3.288787 | 0.318093 | 0.879482 | 89.975% |
| 0.25 | 0 | 156484.4 | 6.309% | 7.679215 | 13.181% | 0.212852 | 2.839872 | 0.322603 | 0.880877 | 89.699% |
| 0.5 | 0 | 165089.4 | 12.155% | 6.067722 | 31.400% | 0.171000 | 1.980151 | 0.258480 | 0.875654 | 87.811% |
| 1 | 0 | 176953.9 | 20.215% | 3.999305 | 54.785% | 0.107930 | 1.651356 | 0.324231 | 0.847800 | 82.461% |
| 2 | 0 | 193524.2 | 31.472% | 3.289175 | 62.813% | 0.082695 | 1.606890 | 0.399042 | 0.828583 | 78.643% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
