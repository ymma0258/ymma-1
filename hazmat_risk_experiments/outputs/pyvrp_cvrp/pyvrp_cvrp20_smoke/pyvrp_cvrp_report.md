# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `20`
- Vehicles: `4`
- Capacity: `5`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 87689.0 | 0.000% | 2.876600 | 0.000% | 0.020845 | 2.841635 | 0.743922 | 0.921308 | 100.000% |
| 0.5 | 96372.0 | 9.902% | 1.953740 | 32.082% | 0.013759 | 1.953740 | 0.750000 | 0.950060 | 100.000% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
