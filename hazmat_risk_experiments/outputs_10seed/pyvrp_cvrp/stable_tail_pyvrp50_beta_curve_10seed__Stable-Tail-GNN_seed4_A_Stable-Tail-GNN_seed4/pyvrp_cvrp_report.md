# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.651668 | 0.000% | 0.269117 | 2.477327 | 0.142433 | 0.874600 | 89.967% |
| 0.25 | 0 | 143612.7 | 7.176% | 6.293020 | 27.262% | 0.196017 | 2.025071 | 0.253990 | 0.868080 | 87.996% |
| 0.5 | 0 | 150422.7 | 12.258% | 4.918940 | 43.145% | 0.140057 | 1.362890 | 0.207604 | 0.848189 | 84.865% |
| 1 | 0 | 160054.1 | 19.445% | 3.409976 | 60.586% | 0.075068 | 1.160148 | 0.294724 | 0.811652 | 78.952% |
| 2 | 0 | 175033.4 | 30.624% | 2.717872 | 68.586% | 0.053936 | 1.087239 | 0.331742 | 0.773170 | 73.438% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
