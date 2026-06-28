# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.136528 | 0.000% | 0.258161 | 2.665513 | 0.222788 | 0.881404 | 90.543% |
| 1 | 0 | 176831.7 | 20.514% | 3.060035 | 62.391% | 0.066624 | 1.217403 | 0.305537 | 0.819271 | 78.920% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
