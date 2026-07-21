# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 7.458772 | 0.000% | 0.196572 | 2.504607 | 0.247568 | 0.876071 | 89.423% |
| 0.25 | 0 | 157050.3 | 6.694% | 6.220026 | 16.608% | 0.152228 | 2.247593 | 0.266762 | 0.869783 | 87.908% |
| 0.5 | 0 | 165286.0 | 12.289% | 4.349386 | 41.688% | 0.109880 | 1.410726 | 0.233227 | 0.847328 | 83.863% |
| 1 | 0 | 175830.0 | 19.452% | 3.110868 | 58.292% | 0.070402 | 1.187494 | 0.289055 | 0.810953 | 78.139% |
| 2 | 0 | 191196.4 | 29.891% | 2.420898 | 67.543% | 0.050839 | 0.925826 | 0.288389 | 0.775254 | 72.142% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
