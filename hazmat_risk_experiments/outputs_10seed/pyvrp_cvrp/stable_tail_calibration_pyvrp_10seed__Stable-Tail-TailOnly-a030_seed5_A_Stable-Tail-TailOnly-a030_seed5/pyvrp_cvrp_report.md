# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.801262 | 0.000% | 0.240450 | 2.310995 | 0.168876 | 0.878091 | 89.528% |
| 0.25 | 0 | 142092.2 | 6.041% | 5.303198 | 32.021% | 0.150791 | 1.692753 | 0.229025 | 0.864938 | 86.998% |
| 0.5 | 0 | 147778.5 | 10.284% | 3.579212 | 54.120% | 0.104593 | 1.306889 | 0.291274 | 0.828350 | 81.279% |
| 1 | 0 | 154760.6 | 15.495% | 2.533468 | 67.525% | 0.065743 | 0.951399 | 0.278735 | 0.773017 | 73.931% |
| 2 | 0 | 165376.7 | 23.417% | 1.924266 | 75.334% | 0.042331 | 0.618566 | 0.222775 | 0.720671 | 66.301% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
