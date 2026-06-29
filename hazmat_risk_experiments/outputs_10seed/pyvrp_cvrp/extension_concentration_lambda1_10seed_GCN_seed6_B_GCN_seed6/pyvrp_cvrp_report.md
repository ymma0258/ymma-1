# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.087849 | 0.000% | 0.287981 | 3.104612 | 0.234715 | 0.869422 | 90.051% |
| 1 | 0 | 180947.7 | 23.319% | 4.617417 | 49.191% | 0.105409 | 1.631656 | 0.318758 | 0.839143 | 83.523% |
| 1 | 1 | 200208.9 | 36.446% | 3.957090 | 56.457% | 0.084104 | 1.521411 | 0.332849 | 0.827901 | 81.224% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
