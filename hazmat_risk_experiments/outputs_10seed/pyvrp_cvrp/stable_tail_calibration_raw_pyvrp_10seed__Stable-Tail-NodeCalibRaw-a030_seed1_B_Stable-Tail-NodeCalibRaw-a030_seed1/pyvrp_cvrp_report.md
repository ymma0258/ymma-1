# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.7 | 0.000% | 10.073454 | 0.000% | 0.319565 | 3.594532 | 0.270657 | 0.872689 | 89.973% |
| 0.25 | 0 | 156087.8 | 5.992% | 8.509221 | 15.528% | 0.263795 | 2.883460 | 0.231976 | 0.870010 | 89.018% |
| 0.5 | 0 | 164604.7 | 11.775% | 6.836112 | 32.137% | 0.195919 | 2.013438 | 0.201765 | 0.862569 | 87.141% |
| 1 | 0 | 174503.6 | 18.497% | 4.080520 | 59.492% | 0.091634 | 1.431755 | 0.269647 | 0.817176 | 79.566% |
| 2 | 0 | 187779.0 | 27.512% | 3.308125 | 67.160% | 0.066573 | 1.167016 | 0.242831 | 0.794951 | 75.573% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
