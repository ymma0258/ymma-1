# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.651668 | 0.000% | 0.269117 | 2.477326 | 0.142433 | 0.874600 | 89.967% |
| 1 | 0 | 160108.7 | 19.486% | 3.394645 | 60.763% | 0.074648 | 1.162602 | 0.297364 | 0.810110 | 78.756% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
