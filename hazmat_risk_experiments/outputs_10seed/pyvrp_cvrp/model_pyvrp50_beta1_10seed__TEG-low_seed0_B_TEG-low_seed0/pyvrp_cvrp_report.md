# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.667610 | 0.000% | 0.252714 | 2.692394 | 0.194748 | 0.841308 | 87.391% |
| 1 | 0 | 178449.7 | 21.617% | 3.586248 | 58.625% | 0.075606 | 1.221459 | 0.237710 | 0.717435 | 71.381% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
