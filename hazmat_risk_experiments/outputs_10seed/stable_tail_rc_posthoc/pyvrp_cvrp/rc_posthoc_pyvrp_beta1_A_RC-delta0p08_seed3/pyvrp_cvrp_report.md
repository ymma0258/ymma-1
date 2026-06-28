# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.845251 | 0.000% | 0.199851 | 2.230452 | 0.215572 | 0.875254 | 89.211% |
| 1 | 0 | 154737.3 | 15.478% | 2.445750 | 64.271% | 0.056797 | 0.844956 | 0.251728 | 0.772973 | 74.687% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
