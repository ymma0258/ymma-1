# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 9.016874 | 0.000% | 0.296667 | 2.552052 | 0.172495 | 0.873998 | 89.659% |
| 0.25 | 0 | 143127.4 | 6.760% | 6.261763 | 30.555% | 0.183911 | 2.062807 | 0.230439 | 0.862309 | 87.294% |
| 0.5 | 0 | 149192.0 | 11.284% | 4.591458 | 49.079% | 0.134733 | 1.542839 | 0.217028 | 0.837685 | 83.375% |
| 1 | 0 | 158422.0 | 18.168% | 3.242868 | 64.036% | 0.085067 | 1.231228 | 0.301769 | 0.796130 | 76.878% |
| 2 | 0 | 171749.8 | 28.110% | 2.649769 | 70.613% | 0.060760 | 0.843506 | 0.252089 | 0.766412 | 72.102% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
