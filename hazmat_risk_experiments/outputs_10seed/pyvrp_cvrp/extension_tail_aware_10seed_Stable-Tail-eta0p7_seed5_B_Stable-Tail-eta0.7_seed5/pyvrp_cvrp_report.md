# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.034169 | 0.000% | 0.219217 | 3.343867 | 0.225794 | 0.879425 | 89.580% |
| 1 | 0 | 173505.2 | 18.247% | 4.018616 | 59.951% | 0.069081 | 1.760732 | 0.361813 | 0.810626 | 77.236% |
| 2 | 0 | 187987.9 | 28.117% | 3.436401 | 65.753% | 0.056289 | 1.303332 | 0.321872 | 0.790373 | 74.239% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
