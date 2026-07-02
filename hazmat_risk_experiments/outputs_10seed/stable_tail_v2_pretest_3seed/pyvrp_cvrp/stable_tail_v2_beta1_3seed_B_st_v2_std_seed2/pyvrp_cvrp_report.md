# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 4.995515 | 0.000% | 0.124835 | 1.560805 | 0.187179 | 0.705489 | 73.792% |
| 1 | 0 | 189524.3 | 29.615% | 3.443846 | 31.061% | 0.055975 | 1.067619 | 0.179973 | 0.617944 | 63.162% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
