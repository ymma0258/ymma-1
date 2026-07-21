# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.4 | 0.000% | 6.655913 | 0.000% | 0.196968 | 2.360367 | 0.256723 | 0.867422 | 88.650% |
| 0.25 | 0 | 155783.7 | 5.929% | 5.910523 | 11.199% | 0.149942 | 2.083694 | 0.247061 | 0.866007 | 88.190% |
| 0.5 | 0 | 163634.5 | 11.267% | 4.446680 | 33.192% | 0.114207 | 1.553859 | 0.241841 | 0.850267 | 85.000% |
| 1 | 0 | 175213.5 | 19.141% | 3.492880 | 47.522% | 0.088598 | 1.376497 | 0.300023 | 0.835344 | 82.014% |
| 2 | 0 | 192835.3 | 31.123% | 2.744073 | 58.772% | 0.067233 | 1.182420 | 0.325917 | 0.805773 | 77.207% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
