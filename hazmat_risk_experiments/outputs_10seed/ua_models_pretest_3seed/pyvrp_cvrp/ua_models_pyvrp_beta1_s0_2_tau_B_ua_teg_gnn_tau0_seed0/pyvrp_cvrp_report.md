# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 8.209670 | 0.000% | 0.242917 | 2.903326 | 0.247520 | 0.880701 | 90.502% |
| 1 | 0 | 177390.0 | 21.317% | 3.490737 | 57.480% | 0.084041 | 1.268623 | 0.313205 | 0.825733 | 80.233% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
