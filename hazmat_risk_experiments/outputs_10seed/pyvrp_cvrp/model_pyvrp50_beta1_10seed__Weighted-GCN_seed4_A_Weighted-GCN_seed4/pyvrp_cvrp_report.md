# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.890465 | 0.000% | 0.283836 | 2.498517 | 0.126087 | 0.843976 | 87.407% |
| 1 | 0 | 163004.6 | 21.647% | 4.089031 | 54.007% | 0.107681 | 1.578095 | 0.311558 | 0.761876 | 75.898% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
