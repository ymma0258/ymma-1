# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.7 | 0.000% | 8.232697 | 0.000% | 0.247730 | 2.606419 | 0.198676 | 0.872421 | 89.025% |
| 0.25 | 0 | 143249.0 | 6.691% | 5.567957 | 32.368% | 0.164763 | 1.731624 | 0.208783 | 0.858126 | 87.054% |
| 0.5 | 0 | 149797.3 | 11.569% | 3.961836 | 51.877% | 0.108178 | 1.444161 | 0.238743 | 0.823763 | 81.957% |
| 1 | 0 | 158919.7 | 18.363% | 2.819752 | 65.749% | 0.062311 | 0.959832 | 0.247164 | 0.783715 | 75.896% |
| 2 | 0 | 173928.1 | 29.541% | 2.215198 | 73.093% | 0.045408 | 0.647053 | 0.198844 | 0.741692 | 69.309% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
