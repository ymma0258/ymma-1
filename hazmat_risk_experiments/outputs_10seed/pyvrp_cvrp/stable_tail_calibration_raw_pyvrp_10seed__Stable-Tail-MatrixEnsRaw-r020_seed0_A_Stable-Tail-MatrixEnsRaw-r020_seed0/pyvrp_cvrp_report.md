# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134197.9 | 0.000% | 6.604693 | 0.000% | 0.201694 | 2.067847 | 0.216255 | 0.886925 | 90.728% |
| 0.25 | 0 | 142310.8 | 6.045% | 4.082201 | 38.192% | 0.125077 | 1.391532 | 0.247877 | 0.870596 | 87.612% |
| 0.5 | 0 | 147970.2 | 10.263% | 3.043088 | 53.925% | 0.090238 | 1.244103 | 0.323018 | 0.838991 | 83.387% |
| 1 | 0 | 155681.3 | 16.009% | 1.906180 | 71.139% | 0.042094 | 0.765264 | 0.280027 | 0.780685 | 74.663% |
| 2 | 0 | 167572.2 | 24.869% | 1.401382 | 78.782% | 0.025809 | 0.479555 | 0.258370 | 0.726520 | 66.125% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
