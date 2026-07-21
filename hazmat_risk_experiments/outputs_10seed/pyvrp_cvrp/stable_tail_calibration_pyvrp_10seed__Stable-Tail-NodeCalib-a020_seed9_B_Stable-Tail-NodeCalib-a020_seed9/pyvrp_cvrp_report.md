# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.9 | 0.000% | 8.967861 | 0.000% | 0.284954 | 2.754925 | 0.200840 | 0.870977 | 89.904% |
| 0.25 | 0 | 158139.9 | 7.531% | 7.713053 | 13.992% | 0.226147 | 2.469641 | 0.198285 | 0.869724 | 89.465% |
| 0.5 | 0 | 168111.6 | 14.312% | 5.415244 | 39.615% | 0.156043 | 1.828824 | 0.252182 | 0.848950 | 85.605% |
| 1 | 0 | 179270.2 | 21.900% | 3.378973 | 62.321% | 0.075853 | 1.108331 | 0.234742 | 0.805834 | 78.266% |
| 2 | 0 | 196752.1 | 33.787% | 3.019069 | 66.335% | 0.059396 | 0.974109 | 0.257145 | 0.793370 | 76.267% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
