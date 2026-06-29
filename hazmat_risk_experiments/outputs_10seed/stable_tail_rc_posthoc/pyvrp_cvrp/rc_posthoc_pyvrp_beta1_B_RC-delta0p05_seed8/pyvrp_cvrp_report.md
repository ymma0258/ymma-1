# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.538579 | 0.000% | 0.221239 | 2.395179 | 0.192997 | 0.878049 | 89.061% |
| 1 | 0 | 175245.6 | 19.433% | 3.244446 | 56.962% | 0.083053 | 1.313517 | 0.332035 | 0.817777 | 78.831% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
