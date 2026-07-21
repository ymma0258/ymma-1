# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 4.759006 | 0.000% | 0.141447 | 1.489010 | 0.214396 | 0.885510 | 90.563% |
| 0.25 | 0 | 142291.0 | 6.189% | 2.763282 | 41.936% | 0.082410 | 0.903696 | 0.225494 | 0.860275 | 86.174% |
| 0.5 | 0 | 147777.6 | 10.283% | 2.283968 | 52.007% | 0.068263 | 0.967443 | 0.325536 | 0.844839 | 84.110% |
| 1 | 0 | 155381.6 | 15.958% | 1.414052 | 70.287% | 0.031447 | 0.585543 | 0.308118 | 0.779123 | 74.190% |
| 2 | 0 | 167073.4 | 24.684% | 1.162460 | 75.573% | 0.021244 | 0.383235 | 0.224930 | 0.746337 | 69.150% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
