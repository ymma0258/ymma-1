# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 6.763494 | 0.000% | 0.204210 | 2.122355 | 0.196359 | 0.873411 | 89.110% |
| 0.25 | 0 | 156318.5 | 6.389% | 5.718681 | 15.448% | 0.152602 | 1.879911 | 0.219462 | 0.869303 | 87.987% |
| 0.5 | 0 | 164960.9 | 12.271% | 4.224550 | 37.539% | 0.115195 | 1.510588 | 0.298158 | 0.845801 | 84.195% |
| 1 | 0 | 175211.8 | 19.248% | 3.070519 | 54.602% | 0.078572 | 1.291685 | 0.337647 | 0.816895 | 79.596% |
| 2 | 0 | 191832.2 | 30.560% | 2.478446 | 63.356% | 0.050345 | 0.915407 | 0.286064 | 0.797355 | 76.459% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
