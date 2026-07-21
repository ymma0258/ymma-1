# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.9 | 0.000% | 7.971969 | 0.000% | 0.240298 | 2.589722 | 0.211313 | 0.869085 | 89.101% |
| 0.25 | 0 | 158149.5 | 7.538% | 7.146276 | 10.357% | 0.190781 | 2.268487 | 0.204570 | 0.867879 | 89.151% |
| 0.5 | 0 | 168481.2 | 14.563% | 5.492290 | 31.105% | 0.134740 | 1.835216 | 0.241994 | 0.855076 | 86.417% |
| 1 | 0 | 181950.1 | 23.722% | 3.870972 | 51.443% | 0.096797 | 1.555203 | 0.348639 | 0.829286 | 81.763% |
| 2 | 0 | 202672.9 | 37.813% | 3.414464 | 57.169% | 0.088222 | 1.241316 | 0.346847 | 0.821135 | 79.877% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
