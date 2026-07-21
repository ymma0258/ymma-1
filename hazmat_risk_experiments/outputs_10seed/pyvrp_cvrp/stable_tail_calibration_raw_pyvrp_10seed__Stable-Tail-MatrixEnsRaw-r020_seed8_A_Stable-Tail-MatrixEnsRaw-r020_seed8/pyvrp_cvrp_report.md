# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 6.251701 | 0.000% | 0.193839 | 1.820290 | 0.168259 | 0.870029 | 88.828% |
| 0.25 | 0 | 142860.9 | 6.561% | 4.206233 | 32.719% | 0.118965 | 1.387965 | 0.243925 | 0.854928 | 86.410% |
| 0.5 | 0 | 149345.8 | 11.398% | 3.329346 | 46.745% | 0.093317 | 1.228864 | 0.257377 | 0.834068 | 83.232% |
| 1 | 0 | 158169.3 | 17.980% | 2.308670 | 63.071% | 0.059324 | 0.713896 | 0.194374 | 0.785871 | 76.285% |
| 2 | 0 | 172876.5 | 28.950% | 1.846521 | 70.464% | 0.034723 | 0.576868 | 0.220729 | 0.754170 | 71.063% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
