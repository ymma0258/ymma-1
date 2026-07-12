# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134597.7 | 0.000% | 8.486439 | 0.000% | 0.279152 | 2.685318 | 0.196367 | 0.879563 | 89.832% |
| 0.25 | 0 | 142553.6 | 5.911% | 5.110342 | 39.782% | 0.137679 | 1.749916 | 0.250045 | 0.864321 | 84.902% |
| 0.5 | 0 | 147546.6 | 9.620% | 4.023647 | 52.587% | 0.101964 | 1.691788 | 0.313166 | 0.850297 | 81.935% |
| 1 | 0 | 156991.4 | 16.638% | 3.014916 | 64.474% | 0.077198 | 1.191330 | 0.305008 | 0.824021 | 76.744% |
| 2 | 0 | 171263.7 | 27.241% | 2.748459 | 67.614% | 0.071213 | 1.207092 | 0.337387 | 0.809906 | 74.595% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
