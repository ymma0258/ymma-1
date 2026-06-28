# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.099662 | 0.000% | 0.294251 | 3.259405 | 0.203251 | 0.879058 | 90.679% |
| 1 | 0 | 177675.8 | 21.090% | 3.930940 | 61.078% | 0.084462 | 1.360828 | 0.272441 | 0.825665 | 79.520% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
