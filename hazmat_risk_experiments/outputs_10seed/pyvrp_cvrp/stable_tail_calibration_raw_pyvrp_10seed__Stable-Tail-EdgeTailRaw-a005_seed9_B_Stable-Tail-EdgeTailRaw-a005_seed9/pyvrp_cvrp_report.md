# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.2 | 0.000% | 8.980667 | 0.000% | 0.278177 | 2.913230 | 0.214261 | 0.870558 | 89.962% |
| 0.25 | 0 | 158927.3 | 8.067% | 7.865405 | 12.418% | 0.235823 | 2.456364 | 0.191054 | 0.868589 | 89.354% |
| 0.5 | 0 | 168419.2 | 14.521% | 4.612963 | 48.635% | 0.122049 | 1.630056 | 0.289500 | 0.836336 | 83.672% |
| 1 | 0 | 179738.1 | 22.217% | 3.485552 | 61.188% | 0.083509 | 1.154742 | 0.256331 | 0.808895 | 78.875% |
| 2 | 0 | 197089.1 | 34.016% | 3.074966 | 65.760% | 0.060342 | 0.962182 | 0.229565 | 0.794065 | 76.536% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
