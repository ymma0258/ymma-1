# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.2 | 0.000% | 9.992734 | 0.000% | 0.298142 | 3.447077 | 0.242037 | 0.875577 | 90.288% |
| 0.25 | 0 | 158378.5 | 7.547% | 8.674621 | 13.191% | 0.211988 | 2.855969 | 0.259577 | 0.876088 | 90.302% |
| 0.5 | 0 | 168864.8 | 14.668% | 7.269477 | 27.252% | 0.181090 | 2.310796 | 0.225841 | 0.870671 | 88.661% |
| 1 | 0 | 181887.7 | 23.511% | 4.453812 | 55.429% | 0.114951 | 1.709177 | 0.341696 | 0.837096 | 82.263% |
| 2 | 0 | 203241.3 | 38.011% | 4.097231 | 58.998% | 0.106270 | 1.622310 | 0.351198 | 0.830138 | 80.821% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
