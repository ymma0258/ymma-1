# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.760996 | 0.000% | 0.243591 | 2.411547 | 0.180304 | 0.880309 | 89.758% |
| 1 | 0 | 155007.6 | 15.679% | 2.614960 | 66.306% | 0.061735 | 0.899936 | 0.243726 | 0.792743 | 75.546% |
| 1 | 0.5 | 159464.6 | 19.006% | 2.229226 | 71.277% | 0.048994 | 0.654099 | 0.210936 | 0.769072 | 71.851% |
| 1 | 1 | 163088.4 | 21.710% | 2.078412 | 73.220% | 0.048172 | 0.607741 | 0.215093 | 0.759437 | 70.207% |
| 1 | 2 | 169721.4 | 26.660% | 1.807715 | 76.708% | 0.033304 | 0.596371 | 0.218495 | 0.714208 | 63.857% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
