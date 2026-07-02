# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 14.779068 | 0.000% | 0.351935 | 4.665054 | 0.201339 | 0.850873 | 88.941% |
| 1.5 | 1 | 217740.1 | 48.394% | 5.406153 | 63.420% | 0.079707 | 2.168248 | 0.347769 | 0.761017 | 75.007% |
| 2 | 1 | 228546.3 | 55.759% | 5.431051 | 63.252% | 0.078337 | 2.076800 | 0.370391 | 0.759539 | 74.741% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
