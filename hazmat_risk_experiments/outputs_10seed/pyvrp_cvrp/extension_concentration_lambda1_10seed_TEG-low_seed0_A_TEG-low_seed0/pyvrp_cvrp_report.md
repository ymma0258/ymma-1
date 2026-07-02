# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.533282 | 0.000% | 0.249183 | 2.663734 | 0.189963 | 0.848031 | 87.588% |
| 1 | 0 | 159882.1 | 19.317% | 3.257919 | 61.821% | 0.076408 | 1.172943 | 0.263857 | 0.723690 | 71.494% |
| 1 | 1 | 168751.4 | 25.936% | 2.389253 | 72.001% | 0.039229 | 0.722327 | 0.211833 | 0.622232 | 59.575% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
