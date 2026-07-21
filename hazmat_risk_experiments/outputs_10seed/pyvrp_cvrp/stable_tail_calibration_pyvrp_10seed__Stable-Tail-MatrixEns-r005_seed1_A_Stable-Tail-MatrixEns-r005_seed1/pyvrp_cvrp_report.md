# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 8.446739 | 0.000% | 0.272299 | 2.262033 | 0.139478 | 0.871369 | 89.535% |
| 0.25 | 0 | 142024.1 | 5.937% | 6.313410 | 25.256% | 0.192932 | 1.911253 | 0.214834 | 0.867938 | 88.239% |
| 0.5 | 0 | 147970.1 | 10.372% | 4.658412 | 44.850% | 0.129877 | 1.596710 | 0.245964 | 0.844411 | 84.513% |
| 1 | 0 | 156418.9 | 16.674% | 3.006725 | 64.404% | 0.066493 | 0.995686 | 0.234184 | 0.793131 | 76.855% |
| 2 | 0 | 169170.9 | 26.186% | 2.456497 | 70.918% | 0.050170 | 0.745523 | 0.232804 | 0.764550 | 72.228% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
