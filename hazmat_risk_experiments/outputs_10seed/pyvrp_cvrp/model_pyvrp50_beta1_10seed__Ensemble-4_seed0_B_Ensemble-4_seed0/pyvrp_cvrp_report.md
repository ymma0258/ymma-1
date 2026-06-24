# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.128175 | 0.000% | 0.251881 | 2.618406 | 0.212091 | 0.848359 | 88.097% |
| 1 | 0 | 178724.1 | 21.804% | 3.543982 | 56.399% | 0.070124 | 1.124930 | 0.245494 | 0.762083 | 75.973% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
