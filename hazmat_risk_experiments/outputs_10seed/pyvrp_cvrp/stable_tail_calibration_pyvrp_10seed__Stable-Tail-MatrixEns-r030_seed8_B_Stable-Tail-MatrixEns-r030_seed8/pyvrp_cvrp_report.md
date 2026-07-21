# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 5.335226 | 0.000% | 0.164490 | 1.628799 | 0.191480 | 0.860999 | 87.854% |
| 0.25 | 0 | 156155.1 | 6.278% | 4.350858 | 18.450% | 0.100434 | 1.482717 | 0.231136 | 0.853846 | 86.724% |
| 0.5 | 0 | 164778.8 | 12.147% | 3.313161 | 37.900% | 0.079829 | 1.122704 | 0.257931 | 0.832919 | 83.238% |
| 1 | 0 | 175329.5 | 19.328% | 2.247523 | 57.874% | 0.054269 | 0.792606 | 0.238284 | 0.790133 | 76.662% |
| 2 | 0 | 189910.9 | 29.252% | 1.693057 | 68.266% | 0.036116 | 0.502248 | 0.215409 | 0.749425 | 70.082% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
