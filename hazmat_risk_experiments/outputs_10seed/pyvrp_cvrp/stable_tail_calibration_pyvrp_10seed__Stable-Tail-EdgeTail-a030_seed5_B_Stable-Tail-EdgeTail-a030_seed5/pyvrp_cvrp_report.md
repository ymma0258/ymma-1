# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.816074 | 0.000% | 0.243637 | 2.558659 | 0.221821 | 0.875252 | 89.111% |
| 0.25 | 0 | 156074.0 | 6.223% | 6.674639 | 14.604% | 0.173615 | 2.187827 | 0.236314 | 0.873285 | 88.611% |
| 0.5 | 0 | 164441.2 | 11.918% | 5.031337 | 35.628% | 0.119257 | 1.725686 | 0.256176 | 0.846089 | 84.618% |
| 1 | 0 | 174630.0 | 18.852% | 3.473400 | 55.561% | 0.085157 | 1.230140 | 0.286155 | 0.816827 | 79.381% |
| 2 | 0 | 190669.3 | 29.768% | 2.833446 | 63.748% | 0.069136 | 0.993756 | 0.301249 | 0.794538 | 75.542% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
