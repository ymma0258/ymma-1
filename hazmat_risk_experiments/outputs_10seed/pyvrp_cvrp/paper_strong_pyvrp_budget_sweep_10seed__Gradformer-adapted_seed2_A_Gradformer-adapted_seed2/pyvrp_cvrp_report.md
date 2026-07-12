# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.6 | 0.000% | 9.148918 | 0.000% | 0.284256 | 2.729696 | 0.180785 | 0.878280 | 90.713% |
| 0.25 | 0 | 144651.0 | 7.682% | 5.979964 | 34.637% | 0.176055 | 2.078758 | 0.266232 | 0.871023 | 87.802% |
| 0.5 | 0 | 152383.8 | 13.439% | 5.107780 | 44.171% | 0.146211 | 1.844779 | 0.280286 | 0.861525 | 86.120% |
| 1 | 0 | 163546.8 | 21.749% | 3.789185 | 58.583% | 0.086404 | 1.282496 | 0.281391 | 0.835212 | 81.666% |
| 2 | 0 | 183021.6 | 36.246% | 2.963408 | 67.609% | 0.065875 | 1.206519 | 0.351818 | 0.804282 | 76.191% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
