# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.090185 | 0.000% | 0.231592 | 2.749108 | 0.245341 | 0.880025 | 90.306% |
| 1 | 0 | 172580.4 | 17.617% | 2.539816 | 68.606% | 0.050024 | 0.917772 | 0.285589 | 0.784574 | 73.927% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
