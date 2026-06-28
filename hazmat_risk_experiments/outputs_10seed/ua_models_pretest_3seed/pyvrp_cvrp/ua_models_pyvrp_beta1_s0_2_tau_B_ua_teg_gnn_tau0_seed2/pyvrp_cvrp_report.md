# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 5.087028 | 0.000% | 0.165948 | 2.045049 | 0.305660 | 0.887903 | 91.954% |
| 1 | 0 | 174873.7 | 19.596% | 2.434980 | 52.134% | 0.067740 | 1.150562 | 0.440206 | 0.845455 | 84.582% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
