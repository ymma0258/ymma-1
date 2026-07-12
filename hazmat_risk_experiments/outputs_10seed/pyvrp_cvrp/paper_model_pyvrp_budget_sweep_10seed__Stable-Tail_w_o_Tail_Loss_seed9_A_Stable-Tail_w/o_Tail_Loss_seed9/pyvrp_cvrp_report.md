# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 6.819361 | 0.000% | 0.211549 | 1.826437 | 0.156208 | 0.875764 | 90.242% |
| 0.25 | 0 | 142684.2 | 6.376% | 5.060726 | 25.789% | 0.164044 | 1.437575 | 0.175205 | 0.870900 | 89.041% |
| 0.5 | 0 | 149747.9 | 11.643% | 4.008625 | 41.217% | 0.126559 | 1.411120 | 0.245014 | 0.861611 | 86.810% |
| 1 | 0 | 159776.1 | 19.119% | 2.966923 | 56.493% | 0.085752 | 0.954386 | 0.215312 | 0.827846 | 81.809% |
| 2 | 0 | 175216.9 | 30.631% | 2.347617 | 65.574% | 0.061212 | 0.843357 | 0.282247 | 0.805888 | 77.560% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
