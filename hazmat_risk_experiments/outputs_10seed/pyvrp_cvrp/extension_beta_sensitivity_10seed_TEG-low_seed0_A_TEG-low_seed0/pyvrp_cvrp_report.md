# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.355225 | 0.000% | 0.238039 | 2.580661 | 0.191426 | 0.845731 | 87.330% |
| 0.5 | 0 | 150236.2 | 12.119% | 4.705795 | 43.678% | 0.131355 | 2.227228 | 0.367739 | 0.790771 | 80.430% |
| 1 | 0 | 159882.2 | 19.317% | 3.258230 | 61.004% | 0.076408 | 1.173070 | 0.263136 | 0.723506 | 71.488% |
| 1.5 | 0 | 167767.2 | 25.202% | 2.731732 | 67.305% | 0.051372 | 0.860048 | 0.220328 | 0.670247 | 65.327% |
| 2 | 0 | 173911.1 | 29.787% | 2.200741 | 73.660% | 0.035137 | 0.774874 | 0.259347 | 0.600661 | 56.929% |
| 3 | 0 | 185495.4 | 38.432% | 2.213401 | 73.509% | 0.035032 | 0.778915 | 0.248981 | 0.606008 | 57.373% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
