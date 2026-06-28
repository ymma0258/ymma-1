# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 13.583217 | 0.000% | 0.227600 | 4.541935 | 0.221259 | 0.846577 | 89.352% |
| 1 | 0 | 181895.7 | 24.398% | 7.518682 | 44.647% | 0.150060 | 2.421399 | 0.226887 | 0.806775 | 82.696% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
