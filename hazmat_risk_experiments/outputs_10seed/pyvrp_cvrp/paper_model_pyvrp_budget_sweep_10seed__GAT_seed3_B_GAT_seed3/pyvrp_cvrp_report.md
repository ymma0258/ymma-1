# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.3 | 0.000% | 7.755753 | 0.000% | 0.235397 | 2.520106 | 0.245536 | 0.854291 | 88.704% |
| 0.25 | 0 | 156620.4 | 6.306% | 6.559881 | 15.419% | 0.170046 | 2.202792 | 0.227869 | 0.849441 | 88.332% |
| 0.5 | 0 | 165334.1 | 12.220% | 5.423320 | 30.074% | 0.135507 | 1.820312 | 0.216203 | 0.837925 | 86.274% |
| 1 | 0 | 178438.2 | 21.114% | 3.964940 | 48.877% | 0.099804 | 1.195495 | 0.196113 | 0.813111 | 81.537% |
| 2 | 0 | 196866.7 | 33.623% | 2.850656 | 63.245% | 0.065954 | 0.904779 | 0.251260 | 0.772749 | 75.016% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
