# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.302978 | 0.000% | 0.243354 | 2.391669 | 0.145524 | 0.860433 | 88.838% |
| 1 | 0 | 160210.3 | 19.562% | 3.368159 | 59.434% | 0.081798 | 1.103775 | 0.270747 | 0.790267 | 77.994% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
