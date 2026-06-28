# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.849915 | 0.000% | 0.235421 | 2.458468 | 0.193165 | 0.829028 | 86.144% |
| 0.5 | 0 | 165267.2 | 12.633% | 5.192836 | 33.848% | 0.121140 | 1.458431 | 0.168998 | 0.789904 | 80.716% |
| 1 | 0 | 177595.1 | 21.035% | 3.642575 | 53.597% | 0.083894 | 1.045124 | 0.200044 | 0.719488 | 72.036% |
| 1.5 | 0 | 186305.7 | 26.971% | 3.088681 | 60.653% | 0.065727 | 0.870106 | 0.175468 | 0.680759 | 67.118% |
| 2 | 0 | 193751.7 | 32.046% | 2.737174 | 65.131% | 0.052646 | 0.919092 | 0.245573 | 0.644857 | 62.648% |
| 3 | 0 | 206745.6 | 40.901% | 2.473549 | 68.489% | 0.040085 | 0.793119 | 0.242265 | 0.615902 | 59.008% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
