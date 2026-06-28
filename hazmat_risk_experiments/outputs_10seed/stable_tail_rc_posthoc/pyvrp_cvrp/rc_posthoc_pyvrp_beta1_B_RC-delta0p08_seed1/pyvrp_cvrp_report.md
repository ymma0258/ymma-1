# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.545074 | 0.000% | 0.244453 | 3.000593 | 0.272467 | 0.883374 | 90.206% |
| 1 | 0 | 173135.7 | 17.995% | 3.229959 | 62.201% | 0.068578 | 1.138166 | 0.289174 | 0.820908 | 78.002% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
