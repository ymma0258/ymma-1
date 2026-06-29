# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.896256 | 0.000% | 0.278367 | 2.507305 | 0.144365 | 0.876659 | 90.176% |
| 1 | 0 | 158165.2 | 18.036% | 3.581226 | 59.745% | 0.098885 | 1.131620 | 0.276123 | 0.823355 | 79.859% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
