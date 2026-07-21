# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147196.9 | 0.000% | 9.642765 | 0.000% | 0.307982 | 3.852359 | 0.335263 | 0.881282 | 90.379% |
| 0.25 | 0 | 156253.9 | 6.153% | 7.762883 | 19.495% | 0.231870 | 3.303592 | 0.361893 | 0.876939 | 89.201% |
| 0.5 | 0 | 164200.7 | 11.552% | 6.641778 | 31.122% | 0.199879 | 2.405223 | 0.280694 | 0.865830 | 87.522% |
| 1 | 0 | 176834.1 | 20.134% | 4.896287 | 49.223% | 0.131334 | 1.995318 | 0.301927 | 0.852684 | 84.604% |
| 2 | 0 | 195212.2 | 32.620% | 3.905630 | 59.497% | 0.101510 | 1.804143 | 0.366879 | 0.835871 | 81.315% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
