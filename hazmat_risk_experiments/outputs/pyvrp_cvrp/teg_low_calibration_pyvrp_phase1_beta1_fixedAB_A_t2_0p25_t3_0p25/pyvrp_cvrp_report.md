# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.254444 | 0.000% | 0.275583 | 2.701754 | 0.225277 | 0.843073 | 87.101% |
| 1 | 0 | 159150.8 | 18.772% | 3.258417 | 60.525% | 0.080045 | 1.201373 | 0.246573 | 0.717224 | 70.611% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
