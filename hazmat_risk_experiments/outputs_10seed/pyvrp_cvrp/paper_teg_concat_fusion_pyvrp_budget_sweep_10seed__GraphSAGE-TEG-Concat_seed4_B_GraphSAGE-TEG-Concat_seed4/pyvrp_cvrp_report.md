# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 9.057234 | 0.000% | 0.271238 | 2.928826 | 0.221988 | 0.880690 | 89.911% |
| 0.25 | 0 | 158443.6 | 7.592% | 7.708779 | 14.888% | 0.214742 | 2.699697 | 0.263106 | 0.878052 | 89.263% |
| 0.5 | 0 | 168054.2 | 14.118% | 5.197143 | 42.619% | 0.128926 | 1.885381 | 0.287127 | 0.851650 | 84.651% |
| 1 | 0 | 180881.3 | 22.828% | 4.429114 | 51.099% | 0.105028 | 1.446666 | 0.260537 | 0.843622 | 82.789% |
| 2 | 0 | 202237.9 | 37.330% | 3.563640 | 60.654% | 0.080553 | 1.357906 | 0.309123 | 0.827680 | 79.436% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
