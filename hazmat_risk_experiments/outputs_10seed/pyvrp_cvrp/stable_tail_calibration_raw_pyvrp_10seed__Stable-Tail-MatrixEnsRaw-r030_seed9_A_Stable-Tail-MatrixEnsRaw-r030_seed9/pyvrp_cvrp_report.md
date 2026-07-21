# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 6.441572 | 0.000% | 0.205860 | 1.905901 | 0.177414 | 0.873955 | 89.729% |
| 0.25 | 0 | 143138.5 | 6.715% | 3.861699 | 40.050% | 0.111167 | 1.233238 | 0.226470 | 0.853297 | 86.745% |
| 0.5 | 0 | 149374.2 | 11.364% | 3.163931 | 50.883% | 0.077259 | 1.238273 | 0.270867 | 0.835158 | 84.348% |
| 1 | 0 | 158396.3 | 18.090% | 2.105295 | 67.317% | 0.049439 | 0.725422 | 0.261535 | 0.778994 | 76.465% |
| 2 | 0 | 172602.4 | 28.681% | 1.764294 | 72.611% | 0.039282 | 0.567850 | 0.225639 | 0.749923 | 72.007% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
