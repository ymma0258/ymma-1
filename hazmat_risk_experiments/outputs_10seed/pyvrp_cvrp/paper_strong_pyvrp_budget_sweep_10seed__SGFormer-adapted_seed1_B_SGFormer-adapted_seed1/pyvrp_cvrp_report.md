# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.2 | 0.000% | 9.043048 | 0.000% | 0.273706 | 2.910400 | 0.231217 | 0.875342 | 89.100% |
| 0.25 | 0 | 157875.7 | 7.109% | 7.350688 | 18.714% | 0.221442 | 2.571620 | 0.254622 | 0.874614 | 87.970% |
| 0.5 | 0 | 166231.1 | 12.778% | 5.153187 | 43.015% | 0.139570 | 1.658427 | 0.248707 | 0.853915 | 83.646% |
| 1 | 0 | 176697.9 | 19.879% | 3.324344 | 63.239% | 0.080299 | 1.108837 | 0.264331 | 0.809514 | 76.307% |
| 2 | 0 | 192540.5 | 30.627% | 2.935279 | 67.541% | 0.065624 | 1.039652 | 0.264734 | 0.797224 | 74.032% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
