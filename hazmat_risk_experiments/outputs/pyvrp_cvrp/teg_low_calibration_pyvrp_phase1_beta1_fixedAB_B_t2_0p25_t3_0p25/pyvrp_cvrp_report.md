# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.431920 | 0.000% | 0.258905 | 2.801004 | 0.225803 | 0.841073 | 87.058% |
| 1 | 0 | 177749.8 | 21.305% | 3.647567 | 56.741% | 0.084779 | 1.290171 | 0.253126 | 0.717612 | 71.098% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
