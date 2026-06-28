# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 10.257497 | 0.000% | 0.251596 | 2.971286 | 0.156540 | 0.853713 | 88.441% |
| 1 | 0 | 160298.9 | 19.628% | 3.984295 | 61.157% | 0.082663 | 1.489548 | 0.268727 | 0.757473 | 75.226% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
