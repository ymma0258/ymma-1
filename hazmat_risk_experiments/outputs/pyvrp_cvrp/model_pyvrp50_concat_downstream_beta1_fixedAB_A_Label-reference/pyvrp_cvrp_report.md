# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 7.986685 | 0.000% | 0.154875 | 2.591347 | 0.199015 | 0.840904 | 86.280% |
| 1 | 0 | 158914.0 | 18.595% | 3.975991 | 50.217% | 0.057499 | 1.516970 | 0.264561 | 0.767982 | 75.216% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
