# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 6.890979 | 0.000% | 0.214305 | 2.240228 | 0.216081 | 0.873637 | 88.885% |
| 0.25 | 0 | 156258.1 | 6.348% | 5.877546 | 14.707% | 0.147940 | 1.877177 | 0.226907 | 0.870716 | 88.290% |
| 0.5 | 0 | 164846.5 | 12.193% | 4.286026 | 37.802% | 0.102561 | 1.360652 | 0.236520 | 0.843312 | 84.143% |
| 1 | 0 | 175311.3 | 19.316% | 3.042305 | 55.851% | 0.073586 | 1.081343 | 0.276570 | 0.812536 | 78.821% |
| 2 | 0 | 191246.2 | 30.161% | 2.498794 | 63.738% | 0.060485 | 0.811752 | 0.266182 | 0.792353 | 75.137% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
