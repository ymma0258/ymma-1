# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.904615 | 0.000% | 0.272518 | 2.788138 | 0.187097 | 0.841212 | 87.122% |
| 1 | 0 | 181548.4 | 23.729% | 4.293602 | 51.782% | 0.084585 | 1.414243 | 0.244848 | 0.752265 | 75.303% |
| 1 | 1 | 197014.3 | 34.269% | 3.364707 | 62.214% | 0.063234 | 1.327782 | 0.268368 | 0.702808 | 68.533% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
