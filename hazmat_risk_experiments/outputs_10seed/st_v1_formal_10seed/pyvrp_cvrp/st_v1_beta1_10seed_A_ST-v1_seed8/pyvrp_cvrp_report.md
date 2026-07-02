# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.474597 | 0.000% | 0.219416 | 2.237541 | 0.159268 | 0.884427 | 90.224% |
| 1 | 0 | 157928.1 | 17.859% | 2.888988 | 61.349% | 0.070160 | 0.880600 | 0.244747 | 0.819804 | 79.393% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
