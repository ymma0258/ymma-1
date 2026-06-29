# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.153544 | 0.000% | 0.163233 | 2.834973 | 0.228214 | 0.875024 | 88.885% |
| 1 | 0 | 172867.3 | 17.812% | 3.645908 | 55.284% | 0.067279 | 1.501019 | 0.321767 | 0.812771 | 78.969% |
| 2 | 0 | 187316.0 | 27.660% | 2.881828 | 64.656% | 0.052843 | 1.142062 | 0.305087 | 0.779416 | 73.653% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
