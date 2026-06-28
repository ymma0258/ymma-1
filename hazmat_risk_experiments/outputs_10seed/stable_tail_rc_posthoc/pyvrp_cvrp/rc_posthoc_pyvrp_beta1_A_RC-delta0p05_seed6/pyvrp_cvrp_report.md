# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.692096 | 0.000% | 0.226307 | 2.182762 | 0.145722 | 0.878024 | 89.510% |
| 1 | 0 | 158962.6 | 18.631% | 2.869799 | 62.692% | 0.074470 | 0.987051 | 0.302151 | 0.805002 | 77.397% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
