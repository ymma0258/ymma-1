# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.6 | 0.000% | 8.651081 | 0.000% | 0.268038 | 2.619485 | 0.185449 | 0.845745 | 87.104% |
| 0.25 | 0 | 144519.7 | 7.478% | 6.046255 | 30.110% | 0.176824 | 1.993739 | 0.245521 | 0.823339 | 83.892% |
| 0.5 | 0 | 152316.6 | 13.276% | 4.995075 | 42.261% | 0.121810 | 1.840058 | 0.296917 | 0.797834 | 80.428% |
| 1 | 0 | 163556.7 | 21.636% | 3.724908 | 56.943% | 0.080106 | 1.260084 | 0.294730 | 0.749776 | 74.176% |
| 2 | 0 | 181805.0 | 35.207% | 2.871022 | 66.813% | 0.050931 | 1.135787 | 0.313977 | 0.685496 | 66.263% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
