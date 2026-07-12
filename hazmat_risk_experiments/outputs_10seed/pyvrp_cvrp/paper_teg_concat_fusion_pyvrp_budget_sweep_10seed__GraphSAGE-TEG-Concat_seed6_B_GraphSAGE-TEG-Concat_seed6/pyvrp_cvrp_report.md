# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.9 | 0.000% | 9.546091 | 0.000% | 0.293295 | 3.004237 | 0.187399 | 0.877601 | 90.207% |
| 0.25 | 0 | 159332.8 | 8.293% | 8.350057 | 12.529% | 0.243357 | 2.638405 | 0.199034 | 0.880010 | 90.270% |
| 0.5 | 0 | 170442.4 | 15.844% | 6.258496 | 34.439% | 0.158832 | 2.190278 | 0.279608 | 0.868681 | 87.534% |
| 1 | 0 | 185121.3 | 25.821% | 4.688604 | 50.885% | 0.103497 | 1.808900 | 0.356428 | 0.853725 | 83.966% |
| 2 | 0 | 210630.2 | 43.158% | 4.208560 | 55.913% | 0.090581 | 1.596006 | 0.360849 | 0.846998 | 82.179% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
