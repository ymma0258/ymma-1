# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 7.018934 | 0.000% | 0.216545 | 2.261399 | 0.194043 | 0.869680 | 88.494% |
| 0.25 | 0 | 141808.3 | 5.566% | 4.959177 | 29.346% | 0.141954 | 1.468912 | 0.176090 | 0.856960 | 86.956% |
| 0.5 | 0 | 147264.8 | 9.628% | 3.638804 | 48.157% | 0.105617 | 1.190604 | 0.212339 | 0.833337 | 82.887% |
| 1 | 0 | 154995.9 | 15.383% | 2.372515 | 66.198% | 0.061573 | 0.690816 | 0.205786 | 0.770321 | 74.196% |
| 2 | 0 | 167358.6 | 24.586% | 2.174656 | 69.017% | 0.052165 | 0.704910 | 0.241715 | 0.754029 | 71.922% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
