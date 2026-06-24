# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.060418 | 0.000% | 0.248541 | 2.620772 | 0.220328 | 0.853823 | 88.372% |
| 1 | 0 | 179330.9 | 22.218% | 3.470404 | 56.945% | 0.083161 | 1.140696 | 0.255421 | 0.781559 | 77.626% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
