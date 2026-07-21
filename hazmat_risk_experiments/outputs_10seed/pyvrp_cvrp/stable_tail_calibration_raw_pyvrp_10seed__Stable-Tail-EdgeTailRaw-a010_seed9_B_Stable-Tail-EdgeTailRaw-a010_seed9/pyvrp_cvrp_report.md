# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 9.062232 | 0.000% | 0.281088 | 2.810567 | 0.202391 | 0.872293 | 90.138% |
| 0.25 | 0 | 158232.3 | 7.545% | 7.955634 | 12.211% | 0.225110 | 2.626786 | 0.221428 | 0.870110 | 89.640% |
| 0.5 | 0 | 167969.1 | 14.163% | 4.998738 | 44.840% | 0.134949 | 1.595411 | 0.258109 | 0.847792 | 84.739% |
| 1 | 0 | 179803.9 | 22.207% | 3.568888 | 60.618% | 0.079569 | 1.366204 | 0.324723 | 0.816682 | 79.930% |
| 2 | 0 | 197099.9 | 33.963% | 3.111169 | 65.669% | 0.061901 | 1.001756 | 0.257452 | 0.797352 | 76.908% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
