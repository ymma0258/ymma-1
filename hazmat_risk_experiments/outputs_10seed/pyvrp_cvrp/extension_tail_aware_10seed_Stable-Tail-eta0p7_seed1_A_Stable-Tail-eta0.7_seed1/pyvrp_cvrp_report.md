# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 10.194934 | 0.000% | 0.178400 | 3.068693 | 0.176995 | 0.877524 | 89.285% |
| 1 | 0 | 156511.9 | 16.802% | 3.643732 | 64.259% | 0.044759 | 1.247671 | 0.228993 | 0.796641 | 75.667% |
| 2 | 0 | 167063.4 | 24.677% | 2.618937 | 74.311% | 0.029671 | 0.797732 | 0.228431 | 0.736719 | 67.039% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
