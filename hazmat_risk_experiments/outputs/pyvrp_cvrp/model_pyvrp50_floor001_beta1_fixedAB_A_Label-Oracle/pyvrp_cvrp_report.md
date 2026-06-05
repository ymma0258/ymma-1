# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.2 | 0.000% | 8.422286 | 0.000% | 0.196493 | 2.847550 | 0.213336 | 0.846269 | 86.988% |
| 1 | 158914.0 | 18.595% | 3.975991 | 52.792% | 0.057499 | 1.516970 | 0.264561 | 0.767982 | 75.216% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
