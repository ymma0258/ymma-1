# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 9.567748 | 0.000% | 0.268366 | 2.856729 | 0.162737 | 0.882099 | 89.755% |
| 1 | 0 | 158666.2 | 18.410% | 3.447197 | 63.971% | 0.093632 | 1.170316 | 0.300783 | 0.810147 | 77.679% |
| 2 | 0 | 172251.2 | 28.548% | 2.806548 | 70.667% | 0.061323 | 1.138804 | 0.321206 | 0.774652 | 72.413% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
