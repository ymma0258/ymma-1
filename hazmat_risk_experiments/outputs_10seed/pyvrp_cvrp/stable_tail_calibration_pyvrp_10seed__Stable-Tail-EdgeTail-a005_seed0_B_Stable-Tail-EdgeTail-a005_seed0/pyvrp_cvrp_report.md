# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147131.1 | 0.000% | 7.347038 | 0.000% | 0.194694 | 2.495478 | 0.252212 | 0.876633 | 89.345% |
| 0.25 | 0 | 157004.9 | 6.711% | 6.416149 | 12.670% | 0.157735 | 2.177851 | 0.255677 | 0.873533 | 88.474% |
| 0.5 | 0 | 165600.0 | 12.553% | 4.524094 | 38.423% | 0.117298 | 1.498547 | 0.240809 | 0.848923 | 84.368% |
| 1 | 0 | 175956.6 | 19.592% | 3.108793 | 57.686% | 0.077323 | 1.099500 | 0.260860 | 0.806614 | 77.800% |
| 2 | 0 | 191335.7 | 30.044% | 2.402272 | 67.303% | 0.047971 | 0.887170 | 0.278486 | 0.774813 | 72.091% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
