# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.767800 | 0.000% | 0.271449 | 2.910150 | 0.221549 | 0.853056 | 88.398% |
| 1 | 0 | 180322.1 | 22.893% | 4.612707 | 47.390% | 0.117673 | 1.480489 | 0.246316 | 0.804672 | 80.800% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
