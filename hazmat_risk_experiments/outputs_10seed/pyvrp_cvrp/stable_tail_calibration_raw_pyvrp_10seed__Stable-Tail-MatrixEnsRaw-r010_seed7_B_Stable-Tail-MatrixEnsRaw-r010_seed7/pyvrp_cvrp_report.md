# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.9 | 0.000% | 9.019031 | 0.000% | 0.272516 | 2.675849 | 0.176997 | 0.878034 | 90.577% |
| 0.25 | 0 | 157593.2 | 7.160% | 7.195856 | 20.215% | 0.202021 | 2.243745 | 0.217064 | 0.875562 | 89.260% |
| 0.5 | 0 | 166943.5 | 13.518% | 5.307088 | 41.157% | 0.149072 | 1.729387 | 0.239067 | 0.858565 | 85.899% |
| 1 | 0 | 178546.8 | 21.408% | 3.493656 | 61.264% | 0.087079 | 1.224470 | 0.263892 | 0.823182 | 79.687% |
| 2 | 0 | 195286.3 | 32.790% | 3.043514 | 66.255% | 0.067717 | 0.968252 | 0.242207 | 0.810634 | 77.424% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
