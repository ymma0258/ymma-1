# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.7 | 0.000% | 7.308079 | 0.000% | 0.224463 | 2.541041 | 0.258846 | 0.872208 | 89.294% |
| 0.25 | 0 | 155350.3 | 5.587% | 5.822497 | 20.328% | 0.142774 | 1.992161 | 0.242418 | 0.865085 | 88.012% |
| 0.5 | 0 | 163402.4 | 11.059% | 4.891684 | 33.065% | 0.123196 | 1.801611 | 0.253638 | 0.855181 | 86.047% |
| 1 | 0 | 174944.5 | 18.904% | 3.328313 | 54.457% | 0.085291 | 1.343801 | 0.319146 | 0.828564 | 81.034% |
| 2 | 0 | 192302.7 | 30.702% | 2.786269 | 61.874% | 0.069948 | 1.115195 | 0.302668 | 0.810177 | 77.810% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
