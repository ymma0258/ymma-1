# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.3 | 0.000% | 7.311497 | 0.000% | 0.231213 | 2.505685 | 0.216544 | 0.865274 | 87.574% |
| 0.25 | 0 | 142113.8 | 5.898% | 5.162662 | 29.390% | 0.144084 | 1.652104 | 0.220606 | 0.852466 | 85.586% |
| 0.5 | 0 | 148132.2 | 10.383% | 3.746748 | 48.755% | 0.103012 | 1.252385 | 0.211259 | 0.818173 | 80.504% |
| 1 | 0 | 155691.5 | 16.016% | 2.511548 | 65.649% | 0.054243 | 0.769850 | 0.208931 | 0.754724 | 71.942% |
| 2 | 0 | 167617.7 | 24.903% | 2.245564 | 69.287% | 0.043876 | 0.701280 | 0.221475 | 0.737299 | 69.325% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
