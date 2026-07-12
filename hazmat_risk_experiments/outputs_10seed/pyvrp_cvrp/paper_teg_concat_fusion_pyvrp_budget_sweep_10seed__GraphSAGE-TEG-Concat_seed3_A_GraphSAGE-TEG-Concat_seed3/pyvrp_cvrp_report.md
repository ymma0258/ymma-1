# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 7.859930 | 0.000% | 0.237929 | 2.392322 | 0.194720 | 0.877717 | 89.571% |
| 0.25 | 0 | 143198.3 | 6.707% | 4.702466 | 40.172% | 0.133150 | 1.573318 | 0.229237 | 0.850579 | 85.115% |
| 0.5 | 0 | 149898.5 | 11.699% | 3.664749 | 53.374% | 0.100408 | 1.278641 | 0.279642 | 0.822411 | 81.015% |
| 1 | 0 | 157737.6 | 17.541% | 2.334461 | 70.299% | 0.046728 | 0.879331 | 0.279661 | 0.756908 | 70.964% |
| 2 | 0 | 168980.0 | 25.918% | 1.726010 | 78.040% | 0.030450 | 0.486790 | 0.162478 | 0.693246 | 61.854% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
