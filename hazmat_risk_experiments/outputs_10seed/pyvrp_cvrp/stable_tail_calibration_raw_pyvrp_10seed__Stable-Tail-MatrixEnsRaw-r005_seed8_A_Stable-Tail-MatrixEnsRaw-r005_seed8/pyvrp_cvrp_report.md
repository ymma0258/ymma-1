# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.499933 | 0.000% | 0.229373 | 2.176247 | 0.164571 | 0.870010 | 88.774% |
| 0.25 | 0 | 142917.4 | 6.656% | 5.207050 | 30.572% | 0.147606 | 1.636163 | 0.232243 | 0.858499 | 86.979% |
| 0.5 | 0 | 149324.4 | 11.438% | 3.915666 | 47.791% | 0.110640 | 1.508962 | 0.284016 | 0.835430 | 83.221% |
| 1 | 0 | 158436.3 | 18.238% | 2.641443 | 64.780% | 0.064538 | 0.815641 | 0.194455 | 0.783757 | 75.854% |
| 2 | 0 | 173440.5 | 29.435% | 2.181565 | 70.912% | 0.042420 | 0.672756 | 0.225678 | 0.754235 | 71.180% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
