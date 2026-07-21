# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.4 | 0.000% | 7.878350 | 0.000% | 0.242823 | 2.876816 | 0.300442 | 0.874157 | 89.518% |
| 0.25 | 0 | 156596.8 | 6.530% | 6.848031 | 13.078% | 0.203738 | 2.731943 | 0.332783 | 0.872553 | 89.052% |
| 0.5 | 0 | 165189.4 | 12.376% | 5.421283 | 31.188% | 0.155316 | 2.090769 | 0.280798 | 0.858191 | 86.543% |
| 1 | 0 | 177643.7 | 20.848% | 4.068444 | 48.359% | 0.110696 | 1.675520 | 0.304339 | 0.846508 | 83.636% |
| 2 | 0 | 196677.9 | 33.797% | 3.177117 | 59.673% | 0.078587 | 1.516181 | 0.386578 | 0.823777 | 79.545% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
