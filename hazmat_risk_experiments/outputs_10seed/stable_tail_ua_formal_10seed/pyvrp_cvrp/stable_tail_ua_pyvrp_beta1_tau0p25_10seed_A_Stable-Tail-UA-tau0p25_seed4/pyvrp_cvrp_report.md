# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 11.281493 | 0.000% | 0.278192 | 3.127426 | 0.135664 | 0.857543 | 89.022% |
| 1 | 0 | 163100.8 | 21.719% | 4.649543 | 58.786% | 0.097950 | 1.653447 | 0.287846 | 0.783242 | 77.762% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
