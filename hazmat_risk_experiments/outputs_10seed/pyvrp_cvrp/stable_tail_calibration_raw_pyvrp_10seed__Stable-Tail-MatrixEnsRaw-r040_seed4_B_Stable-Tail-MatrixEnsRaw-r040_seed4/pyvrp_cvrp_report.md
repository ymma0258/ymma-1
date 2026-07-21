# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.9 | 0.000% | 5.315855 | 0.000% | 0.158743 | 1.675710 | 0.206845 | 0.877770 | 89.644% |
| 0.25 | 0 | 156365.4 | 6.325% | 4.565022 | 14.124% | 0.129633 | 1.437495 | 0.203388 | 0.873430 | 88.778% |
| 0.5 | 0 | 164742.3 | 12.021% | 3.496680 | 34.222% | 0.093161 | 1.116265 | 0.238076 | 0.859361 | 85.962% |
| 1 | 0 | 175328.4 | 19.219% | 2.321694 | 56.325% | 0.058046 | 0.934515 | 0.316592 | 0.820355 | 79.866% |
| 2 | 0 | 191487.0 | 30.207% | 2.015846 | 62.079% | 0.043996 | 0.771814 | 0.315869 | 0.805382 | 77.531% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
