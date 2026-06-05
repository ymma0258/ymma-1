# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 11.331718 | 0.000% | 0.182951 | 3.643733 | 0.218736 | 0.842325 | 87.397% |
| 1 | 179502.4 | 22.501% | 4.597304 | 59.430% | 0.079317 | 1.532349 | 0.263920 | 0.710183 | 69.978% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
