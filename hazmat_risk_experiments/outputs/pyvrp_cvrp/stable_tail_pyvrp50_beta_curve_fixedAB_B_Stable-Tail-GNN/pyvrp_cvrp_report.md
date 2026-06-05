# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 7.782682 | 0.000% | 0.244204 | 2.694265 | 0.248715 | 0.882545 | 90.603% |
| 0.25 | 0 | 156968.2 | 7.123% | 6.716989 | 13.693% | 0.192885 | 2.182795 | 0.229562 | 0.881802 | 89.809% |
| 0.5 | 0 | 166120.8 | 13.369% | 4.791507 | 38.434% | 0.132376 | 1.384830 | 0.192707 | 0.862435 | 86.067% |
| 1 | 0 | 176686.4 | 20.579% | 2.983237 | 61.668% | 0.062350 | 1.036451 | 0.276663 | 0.818129 | 78.827% |
| 2 | 0 | 191396.4 | 30.618% | 2.455709 | 68.447% | 0.051278 | 0.986971 | 0.310977 | 0.789363 | 74.040% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
