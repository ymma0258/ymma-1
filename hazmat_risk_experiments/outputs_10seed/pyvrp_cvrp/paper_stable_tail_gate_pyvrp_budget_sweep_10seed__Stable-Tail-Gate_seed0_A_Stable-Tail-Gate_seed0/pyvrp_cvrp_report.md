# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.8 | 0.000% | 8.312665 | 0.000% | 0.250115 | 2.463703 | 0.174361 | 0.858508 | 88.089% |
| 0.25 | 0 | 142561.8 | 6.338% | 5.338106 | 35.783% | 0.150430 | 1.472811 | 0.123965 | 0.834949 | 85.408% |
| 0.5 | 0 | 148751.7 | 10.955% | 4.385984 | 47.237% | 0.124890 | 1.447946 | 0.233153 | 0.816967 | 82.894% |
| 1 | 0 | 157344.8 | 17.365% | 2.790275 | 66.433% | 0.057871 | 1.088086 | 0.308606 | 0.739981 | 73.182% |
| 2 | 0 | 170207.1 | 26.959% | 2.197034 | 73.570% | 0.040477 | 0.652926 | 0.222944 | 0.690218 | 66.365% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
