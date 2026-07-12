# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 9.237591 | 0.000% | 0.270978 | 2.626066 | 0.148083 | 0.853652 | 88.182% |
| 0.25 | 0 | 144131.8 | 7.563% | 7.237928 | 21.647% | 0.212383 | 2.153267 | 0.209830 | 0.848064 | 87.632% |
| 0.5 | 0 | 151717.1 | 13.223% | 5.143229 | 44.323% | 0.152190 | 1.908980 | 0.272796 | 0.814855 | 82.808% |
| 1 | 0 | 162070.0 | 20.949% | 3.642355 | 60.570% | 0.089006 | 1.276607 | 0.292676 | 0.766252 | 76.123% |
| 2 | 0 | 177844.7 | 32.722% | 2.629323 | 71.537% | 0.045735 | 0.963775 | 0.325826 | 0.696488 | 67.032% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
