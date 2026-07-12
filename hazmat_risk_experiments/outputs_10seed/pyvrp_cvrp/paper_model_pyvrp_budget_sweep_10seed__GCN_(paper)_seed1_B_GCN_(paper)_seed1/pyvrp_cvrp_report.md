# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 8.467782 | 0.000% | 0.258561 | 2.752666 | 0.209696 | 0.865961 | 89.023% |
| 0.25 | 0 | 156740.3 | 6.628% | 7.409522 | 12.497% | 0.182979 | 2.480064 | 0.230155 | 0.864468 | 88.883% |
| 0.5 | 0 | 165645.0 | 12.686% | 5.379439 | 36.472% | 0.134941 | 1.889011 | 0.259499 | 0.845035 | 85.104% |
| 1 | 0 | 176884.8 | 20.332% | 3.578191 | 57.743% | 0.089124 | 1.175207 | 0.250653 | 0.801792 | 78.764% |
| 2 | 0 | 193837.9 | 31.865% | 2.941873 | 65.258% | 0.069164 | 0.900008 | 0.227062 | 0.777482 | 74.521% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
