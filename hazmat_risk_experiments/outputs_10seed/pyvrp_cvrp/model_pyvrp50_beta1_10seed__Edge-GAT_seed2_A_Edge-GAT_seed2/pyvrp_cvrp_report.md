# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.010790 | 0.000% | 0.248405 | 2.328009 | 0.161393 | 0.870460 | 89.478% |
| 1 | 0 | 158534.2 | 18.311% | 3.446036 | 56.983% | 0.090699 | 1.097148 | 0.270350 | 0.812125 | 79.756% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
