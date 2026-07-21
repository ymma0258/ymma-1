# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.1 | 0.000% | 7.396319 | 0.000% | 0.197308 | 2.537385 | 0.265097 | 0.877398 | 89.505% |
| 0.25 | 0 | 156723.0 | 6.327% | 6.403327 | 13.425% | 0.156534 | 1.992276 | 0.204350 | 0.874048 | 88.463% |
| 0.5 | 0 | 165320.9 | 12.160% | 4.480969 | 39.416% | 0.113301 | 1.429845 | 0.235835 | 0.849508 | 84.141% |
| 1 | 0 | 175724.5 | 19.218% | 3.124957 | 57.750% | 0.079317 | 1.083804 | 0.246710 | 0.811426 | 78.215% |
| 2 | 0 | 191401.3 | 29.854% | 2.410747 | 67.406% | 0.048746 | 0.971234 | 0.313693 | 0.776376 | 72.152% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
