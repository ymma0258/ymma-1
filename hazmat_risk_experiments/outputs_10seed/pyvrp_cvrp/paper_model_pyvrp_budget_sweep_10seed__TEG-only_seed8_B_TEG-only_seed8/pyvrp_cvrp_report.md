# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147131.0 | 0.000% | 8.423935 | 0.000% | 0.245928 | 2.722511 | 0.216642 | 0.826903 | 86.122% |
| 0.25 | 0 | 157061.7 | 6.750% | 7.522733 | 10.698% | 0.212452 | 2.400778 | 0.210936 | 0.823507 | 85.537% |
| 0.5 | 0 | 165773.3 | 12.671% | 6.354052 | 24.571% | 0.168520 | 1.908500 | 0.192283 | 0.805406 | 83.014% |
| 1 | 0 | 177867.8 | 20.891% | 4.274712 | 49.255% | 0.084988 | 1.444705 | 0.251485 | 0.744295 | 75.215% |
| 2 | 0 | 193691.0 | 31.645% | 3.227932 | 61.681% | 0.053839 | 1.029240 | 0.229051 | 0.680067 | 66.875% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
