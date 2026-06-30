# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.003160 | 0.000% | 0.253942 | 2.625387 | 0.223399 | 0.881536 | 90.545% |
| 1.5 | 1 | 197547.4 | 34.632% | 2.209697 | 72.390% | 0.046114 | 0.990779 | 0.336962 | 0.774545 | 71.337% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
