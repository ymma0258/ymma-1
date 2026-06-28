# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 7.128572 | 0.000% | 0.227334 | 2.182399 | 0.172896 | 0.858457 | 88.994% |
| 1 | 0 | 159397.3 | 18.956% | 2.834067 | 60.244% | 0.069016 | 0.924853 | 0.231021 | 0.783750 | 77.881% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
