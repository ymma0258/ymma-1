# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.422272 | 0.000% | 0.222439 | 2.328080 | 0.192792 | 0.831738 | 85.825% |
| 1 | 0 | 158033.9 | 17.938% | 3.055585 | 58.832% | 0.073665 | 0.963350 | 0.219694 | 0.697502 | 69.253% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
