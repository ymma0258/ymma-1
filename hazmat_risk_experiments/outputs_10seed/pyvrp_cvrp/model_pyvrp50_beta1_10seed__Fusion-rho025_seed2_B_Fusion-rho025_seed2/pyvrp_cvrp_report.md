# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.698808 | 0.000% | 0.300642 | 3.338207 | 0.255183 | 0.860778 | 89.578% |
| 1 | 0 | 180354.9 | 22.915% | 5.070561 | 47.720% | 0.142716 | 1.998087 | 0.316630 | 0.831835 | 83.504% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
