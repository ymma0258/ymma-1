# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.701649 | 0.000% | 0.270892 | 2.469651 | 0.147285 | 0.874652 | 89.737% |
| 1 | 0 | 158504.1 | 18.289% | 3.241617 | 62.747% | 0.072378 | 1.172913 | 0.287471 | 0.804383 | 77.587% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
