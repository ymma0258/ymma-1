# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 9.192140 | 0.000% | 0.298004 | 2.503541 | 0.156345 | 0.877547 | 89.952% |
| 0.25 | 0 | 143620.4 | 6.915% | 6.215035 | 32.388% | 0.185310 | 1.828304 | 0.195006 | 0.866431 | 88.003% |
| 0.5 | 0 | 150308.0 | 11.893% | 4.635285 | 49.573% | 0.137064 | 1.382205 | 0.221584 | 0.845887 | 84.480% |
| 1 | 0 | 159688.4 | 18.876% | 3.566790 | 61.197% | 0.091318 | 1.121952 | 0.260297 | 0.817583 | 80.355% |
| 2 | 0 | 175104.4 | 30.353% | 2.830605 | 69.206% | 0.066504 | 1.046663 | 0.329715 | 0.788736 | 75.766% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
