# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 9.657769 | 0.000% | 0.286440 | 3.427657 | 0.268332 | 0.879754 | 91.170% |
| 1 | 0 | 178518.6 | 21.830% | 4.488468 | 53.525% | 0.121941 | 1.653961 | 0.305842 | 0.849488 | 83.293% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
