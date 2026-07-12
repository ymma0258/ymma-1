# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.5 | 0.000% | 9.269615 | 0.000% | 0.303471 | 2.825083 | 0.184797 | 0.862166 | 88.314% |
| 0.25 | 0 | 143985.2 | 7.186% | 5.531007 | 40.332% | 0.138421 | 1.847068 | 0.246120 | 0.833118 | 84.850% |
| 0.5 | 0 | 150642.6 | 12.142% | 4.727622 | 48.999% | 0.126796 | 1.851186 | 0.281973 | 0.816470 | 82.599% |
| 1 | 0 | 160340.8 | 19.362% | 3.207006 | 65.403% | 0.078711 | 1.300630 | 0.316550 | 0.759830 | 74.606% |
| 2 | 0 | 174254.3 | 29.720% | 2.256314 | 75.659% | 0.036758 | 0.775779 | 0.257925 | 0.678680 | 63.608% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
