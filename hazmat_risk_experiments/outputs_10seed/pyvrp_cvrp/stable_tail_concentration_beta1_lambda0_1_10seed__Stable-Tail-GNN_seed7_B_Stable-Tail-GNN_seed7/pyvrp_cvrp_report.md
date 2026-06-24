# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.851676 | 0.000% | 0.287040 | 3.185509 | 0.204509 | 0.879458 | 90.687% |
| 1 | 0 | 177194.1 | 20.761% | 3.710959 | 62.332% | 0.080461 | 1.296403 | 0.270355 | 0.820586 | 78.876% |
| 1 | 1 | 189951.6 | 29.456% | 3.238929 | 67.123% | 0.068575 | 1.027958 | 0.251002 | 0.806733 | 76.248% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
