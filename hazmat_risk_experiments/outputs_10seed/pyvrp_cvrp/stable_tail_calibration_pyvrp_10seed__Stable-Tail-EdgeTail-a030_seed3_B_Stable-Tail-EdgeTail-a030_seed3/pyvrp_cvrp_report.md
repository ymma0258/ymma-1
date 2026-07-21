# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.141119 | 0.000% | 0.218622 | 2.455233 | 0.254273 | 0.871966 | 89.209% |
| 0.25 | 0 | 155263.3 | 5.671% | 5.867306 | 17.838% | 0.149139 | 2.314377 | 0.282695 | 0.865992 | 88.014% |
| 0.5 | 0 | 162970.3 | 10.917% | 4.894465 | 31.461% | 0.124335 | 1.967504 | 0.283066 | 0.856726 | 86.157% |
| 1 | 0 | 174629.8 | 18.852% | 3.388497 | 52.549% | 0.086120 | 1.429903 | 0.316631 | 0.829533 | 81.570% |
| 2 | 0 | 190912.3 | 29.934% | 2.698963 | 62.205% | 0.068096 | 1.189277 | 0.331428 | 0.806120 | 77.182% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
