# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.9 | 0.000% | 10.359321 | 0.000% | 0.313947 | 3.055938 | 0.177714 | 0.880669 | 90.887% |
| 0.25 | 0 | 157835.0 | 7.324% | 7.700666 | 25.664% | 0.212408 | 2.637113 | 0.255494 | 0.876340 | 89.008% |
| 0.5 | 0 | 167210.2 | 13.699% | 5.468157 | 47.215% | 0.152171 | 1.882025 | 0.245358 | 0.852812 | 84.915% |
| 1 | 0 | 178406.4 | 21.312% | 3.967769 | 61.699% | 0.101957 | 1.345391 | 0.247209 | 0.826795 | 80.152% |
| 2 | 0 | 195321.4 | 32.814% | 3.411652 | 67.067% | 0.076434 | 1.056050 | 0.207246 | 0.810762 | 77.424% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
