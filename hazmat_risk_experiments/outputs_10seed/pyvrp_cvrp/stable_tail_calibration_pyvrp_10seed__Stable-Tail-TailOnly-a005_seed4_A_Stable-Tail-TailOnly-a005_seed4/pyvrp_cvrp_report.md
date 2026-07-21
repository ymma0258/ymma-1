# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 9.001894 | 0.000% | 0.282865 | 2.577784 | 0.167302 | 0.878382 | 90.123% |
| 0.25 | 0 | 143385.6 | 6.899% | 6.877308 | 23.602% | 0.215532 | 1.993681 | 0.172983 | 0.874128 | 89.092% |
| 0.5 | 0 | 150275.3 | 12.036% | 4.963702 | 44.859% | 0.151759 | 1.469795 | 0.235371 | 0.850889 | 85.421% |
| 1 | 0 | 159929.5 | 19.233% | 3.533196 | 60.751% | 0.092762 | 1.238857 | 0.311309 | 0.816070 | 80.021% |
| 2 | 0 | 175063.1 | 30.516% | 2.862636 | 68.200% | 0.066261 | 1.062081 | 0.306449 | 0.789938 | 75.877% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
