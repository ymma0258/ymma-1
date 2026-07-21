# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.908012 | 0.000% | 0.235108 | 2.420620 | 0.212973 | 0.885588 | 90.647% |
| 0.25 | 0 | 141626.1 | 5.640% | 4.960543 | 37.272% | 0.151882 | 1.605933 | 0.231783 | 0.868485 | 87.317% |
| 0.5 | 0 | 147100.0 | 9.723% | 3.795222 | 52.008% | 0.114323 | 1.706481 | 0.335602 | 0.843598 | 84.151% |
| 1 | 0 | 154679.0 | 15.376% | 2.414503 | 69.468% | 0.055186 | 1.004671 | 0.315556 | 0.779278 | 74.453% |
| 2 | 0 | 165904.4 | 23.750% | 1.926345 | 75.641% | 0.035244 | 0.675331 | 0.257952 | 0.744059 | 68.955% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
