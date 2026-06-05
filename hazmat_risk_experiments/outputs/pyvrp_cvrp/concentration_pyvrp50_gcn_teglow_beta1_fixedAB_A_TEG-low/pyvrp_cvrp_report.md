# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.096137 | 0.000% | 0.225235 | 2.608916 | 0.213907 | 0.842542 | 87.221% |
| 1 | 0 | 159880.0 | 19.316% | 3.292546 | 59.332% | 0.081298 | 1.144897 | 0.252542 | 0.726400 | 71.886% |
| 1 | 0.5 | 165478.6 | 23.494% | 2.543635 | 68.582% | 0.045264 | 0.817678 | 0.219635 | 0.647100 | 62.584% |
| 1 | 1 | 168757.4 | 25.941% | 2.457405 | 69.647% | 0.040774 | 0.723841 | 0.197358 | 0.632749 | 60.787% |
| 1 | 2 | 175471.0 | 30.951% | 2.153395 | 73.402% | 0.034023 | 0.808156 | 0.276548 | 0.600394 | 56.619% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
