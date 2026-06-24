# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.807039 | 0.000% | 0.237220 | 2.483172 | 0.201673 | 0.824267 | 85.812% |
| 1 | 0 | 179429.8 | 22.285% | 3.484505 | 55.367% | 0.079266 | 1.083107 | 0.208175 | 0.698095 | 69.901% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
