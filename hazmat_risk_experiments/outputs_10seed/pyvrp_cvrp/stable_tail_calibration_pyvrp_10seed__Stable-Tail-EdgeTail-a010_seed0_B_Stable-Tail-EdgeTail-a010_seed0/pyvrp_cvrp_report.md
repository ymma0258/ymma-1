# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.7 | 0.000% | 7.212332 | 0.000% | 0.192651 | 2.469939 | 0.262844 | 0.877598 | 89.254% |
| 0.25 | 0 | 157204.6 | 6.606% | 6.056961 | 16.019% | 0.146965 | 2.310678 | 0.279632 | 0.868604 | 87.723% |
| 0.5 | 0 | 165486.7 | 12.222% | 4.330536 | 39.957% | 0.109095 | 1.475525 | 0.236701 | 0.845378 | 83.764% |
| 1 | 0 | 176459.9 | 19.663% | 3.056563 | 57.620% | 0.075367 | 1.049795 | 0.228660 | 0.807354 | 77.580% |
| 2 | 0 | 190784.0 | 29.377% | 2.386458 | 66.911% | 0.047895 | 0.853894 | 0.262309 | 0.772156 | 71.833% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
