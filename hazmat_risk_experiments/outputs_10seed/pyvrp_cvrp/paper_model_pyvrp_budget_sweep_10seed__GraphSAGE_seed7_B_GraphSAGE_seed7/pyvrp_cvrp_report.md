# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.9 | 0.000% | 9.448713 | 0.000% | 0.294164 | 2.834818 | 0.157751 | 0.871234 | 89.101% |
| 0.25 | 0 | 158485.4 | 7.717% | 8.452389 | 10.545% | 0.247893 | 2.436831 | 0.165404 | 0.873015 | 89.430% |
| 0.5 | 0 | 169318.8 | 15.080% | 6.436388 | 31.881% | 0.158017 | 2.184130 | 0.275509 | 0.862921 | 86.881% |
| 1 | 0 | 182811.9 | 24.251% | 4.647713 | 50.811% | 0.116177 | 1.534958 | 0.242208 | 0.837058 | 82.110% |
| 2 | 0 | 203194.3 | 38.104% | 3.814948 | 59.625% | 0.095973 | 1.260530 | 0.254025 | 0.821468 | 79.010% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
