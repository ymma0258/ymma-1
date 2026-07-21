# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.0 | 0.000% | 9.010074 | 0.000% | 0.272589 | 3.080402 | 0.242144 | 0.870063 | 89.366% |
| 0.25 | 0 | 158163.2 | 7.304% | 7.696452 | 14.579% | 0.188339 | 2.602185 | 0.254116 | 0.869465 | 89.227% |
| 0.5 | 0 | 168575.5 | 14.368% | 6.321444 | 29.840% | 0.155504 | 2.145084 | 0.258005 | 0.857703 | 86.826% |
| 1 | 0 | 181535.0 | 23.161% | 4.234066 | 53.007% | 0.106070 | 1.554922 | 0.328153 | 0.827783 | 81.301% |
| 2 | 0 | 202507.0 | 37.389% | 3.714377 | 58.775% | 0.094537 | 1.419715 | 0.330243 | 0.815724 | 79.021% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
