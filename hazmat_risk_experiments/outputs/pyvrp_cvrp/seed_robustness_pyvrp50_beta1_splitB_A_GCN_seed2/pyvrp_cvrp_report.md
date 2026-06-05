# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.423277 | 0.000% | 0.280436 | 2.502318 | 0.148983 | 0.864645 | 89.372% |
| 1 | 0 | 160114.2 | 19.491% | 3.677509 | 56.341% | 0.105402 | 1.227604 | 0.267363 | 0.811172 | 79.983% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
