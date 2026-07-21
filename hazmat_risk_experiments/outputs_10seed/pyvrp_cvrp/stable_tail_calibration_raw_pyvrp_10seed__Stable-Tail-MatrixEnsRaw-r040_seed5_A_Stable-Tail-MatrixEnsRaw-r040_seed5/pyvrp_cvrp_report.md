# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.3 | 0.000% | 4.581927 | 0.000% | 0.141920 | 1.387672 | 0.181392 | 0.877436 | 89.314% |
| 0.25 | 0 | 142358.9 | 6.134% | 3.195225 | 30.265% | 0.089865 | 1.071167 | 0.251503 | 0.865086 | 86.999% |
| 0.5 | 0 | 147946.5 | 10.300% | 2.238383 | 51.148% | 0.065806 | 0.863405 | 0.322369 | 0.831429 | 82.086% |
| 1 | 0 | 155639.1 | 16.035% | 1.488479 | 67.514% | 0.038070 | 0.632887 | 0.307727 | 0.771414 | 73.430% |
| 2 | 0 | 166475.3 | 24.114% | 1.158480 | 74.716% | 0.025533 | 0.380667 | 0.252448 | 0.724148 | 66.480% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
