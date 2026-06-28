# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 12.484647 | 0.000% | 0.304993 | 3.427479 | 0.142564 | 0.845209 | 88.170% |
| 1 | 0 | 164853.8 | 23.027% | 5.229736 | 58.111% | 0.109100 | 1.928362 | 0.290903 | 0.762631 | 76.525% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
