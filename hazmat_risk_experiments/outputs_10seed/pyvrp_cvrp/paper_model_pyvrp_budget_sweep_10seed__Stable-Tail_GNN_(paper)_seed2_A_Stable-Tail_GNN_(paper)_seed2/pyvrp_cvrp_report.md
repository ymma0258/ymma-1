# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 8.494687 | 0.000% | 0.280242 | 2.659052 | 0.197597 | 0.874287 | 89.386% |
| 0.25 | 0 | 142608.8 | 6.162% | 5.713234 | 32.743% | 0.166544 | 1.921329 | 0.212261 | 0.861385 | 87.307% |
| 0.5 | 0 | 148790.6 | 10.764% | 4.568158 | 46.223% | 0.132490 | 1.506089 | 0.247253 | 0.848718 | 84.675% |
| 1 | 0 | 158091.7 | 17.688% | 3.269570 | 61.510% | 0.084139 | 1.208793 | 0.317167 | 0.809868 | 79.074% |
| 2 | 0 | 172453.3 | 28.379% | 2.866708 | 66.253% | 0.067712 | 1.191263 | 0.332127 | 0.792133 | 75.978% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
