# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 8.471561 | 0.000% | 0.270863 | 2.391950 | 0.162616 | 0.870867 | 89.547% |
| 0.25 | 0 | 143036.9 | 6.693% | 5.790648 | 31.646% | 0.182883 | 1.876016 | 0.224255 | 0.855958 | 87.310% |
| 0.5 | 0 | 149325.6 | 11.383% | 4.479827 | 47.119% | 0.121791 | 1.694113 | 0.266174 | 0.832937 | 84.144% |
| 1 | 0 | 158238.7 | 18.032% | 2.830845 | 66.584% | 0.066106 | 0.998301 | 0.283855 | 0.771481 | 75.304% |
| 2 | 0 | 172453.3 | 28.634% | 2.349762 | 72.263% | 0.050480 | 0.721844 | 0.233024 | 0.736989 | 70.391% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
