# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.277512 | 0.000% | 0.217044 | 3.126709 | 0.229975 | 0.879313 | 89.536% |
| 1 | 0 | 173720.5 | 18.394% | 3.742577 | 59.660% | 0.073777 | 1.567626 | 0.362246 | 0.813840 | 77.850% |
| 2 | 0 | 188617.3 | 28.546% | 3.165997 | 65.875% | 0.063330 | 1.178883 | 0.315528 | 0.791579 | 74.430% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
