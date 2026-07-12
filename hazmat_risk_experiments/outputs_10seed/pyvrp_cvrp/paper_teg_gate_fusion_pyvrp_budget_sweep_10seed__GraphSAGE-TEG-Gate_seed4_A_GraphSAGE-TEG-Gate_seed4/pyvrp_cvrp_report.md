# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.8 | 0.000% | 8.944572 | 0.000% | 0.273636 | 2.592279 | 0.169672 | 0.885095 | 91.076% |
| 0.25 | 0 | 144298.0 | 7.633% | 5.390794 | 39.731% | 0.160783 | 2.012577 | 0.294947 | 0.863047 | 87.107% |
| 0.5 | 0 | 151340.4 | 12.886% | 4.936093 | 44.815% | 0.122103 | 2.010138 | 0.341267 | 0.856849 | 86.181% |
| 1 | 0 | 162197.2 | 20.984% | 3.591473 | 59.847% | 0.084631 | 1.272312 | 0.303668 | 0.825716 | 81.108% |
| 2 | 0 | 176829.5 | 31.899% | 2.289230 | 74.406% | 0.049442 | 0.930180 | 0.349559 | 0.761948 | 70.771% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
