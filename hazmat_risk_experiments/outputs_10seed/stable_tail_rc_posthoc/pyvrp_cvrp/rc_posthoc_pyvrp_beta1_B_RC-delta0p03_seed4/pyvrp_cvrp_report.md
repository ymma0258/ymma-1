# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 9.309402 | 0.000% | 0.293691 | 3.038766 | 0.207518 | 0.876119 | 89.715% |
| 1 | 0 | 177471.2 | 20.786% | 3.798741 | 59.195% | 0.088683 | 1.563089 | 0.322825 | 0.814248 | 78.990% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
