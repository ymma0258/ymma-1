# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.2 | 0.000% | 7.422261 | 0.000% | 0.222776 | 2.635329 | 0.259135 | 0.873733 | 89.580% |
| 0.25 | 0 | 155161.6 | 5.506% | 6.263791 | 15.608% | 0.152172 | 2.470843 | 0.274267 | 0.870078 | 88.638% |
| 0.5 | 0 | 162764.3 | 10.676% | 5.195012 | 30.008% | 0.133700 | 2.010865 | 0.282596 | 0.863518 | 87.086% |
| 1 | 0 | 174307.6 | 18.525% | 3.893186 | 47.547% | 0.102264 | 1.609656 | 0.326654 | 0.847751 | 83.670% |
| 2 | 0 | 191541.4 | 30.243% | 3.023982 | 59.258% | 0.078152 | 1.343004 | 0.317890 | 0.823640 | 79.363% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
