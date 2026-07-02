# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.851676 | 0.000% | 0.287040 | 3.185509 | 0.204509 | 0.879458 | 90.687% |
| 0.5 | 0 | 166654.3 | 13.578% | 6.224514 | 36.818% | 0.161202 | 2.159965 | 0.282387 | 0.864965 | 86.770% |
| 1 | 0 | 177190.3 | 20.759% | 3.710676 | 62.335% | 0.080461 | 1.295202 | 0.270191 | 0.820447 | 78.846% |
| 1.5 | 0 | 185422.7 | 26.369% | 3.350958 | 65.986% | 0.071788 | 1.039671 | 0.251621 | 0.812471 | 77.205% |
| 2 | 0 | 193431.3 | 31.827% | 3.301975 | 66.483% | 0.071917 | 1.026371 | 0.247779 | 0.811350 | 76.963% |
| 3 | 0 | 208552.9 | 42.133% | 3.052953 | 69.011% | 0.066865 | 1.109050 | 0.317693 | 0.802351 | 75.048% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
