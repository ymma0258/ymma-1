# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.9 | 0.000% | 8.355926 | 0.000% | 0.274689 | 2.746235 | 0.221154 | 0.889666 | 91.007% |
| 0.25 | 0 | 142714.4 | 6.293% | 5.731258 | 31.411% | 0.175940 | 1.915129 | 0.239501 | 0.886805 | 90.000% |
| 0.5 | 0 | 149218.8 | 11.138% | 4.365878 | 47.751% | 0.131572 | 1.516790 | 0.280251 | 0.879072 | 87.503% |
| 1 | 0 | 158615.9 | 18.137% | 3.068304 | 63.280% | 0.085033 | 1.179892 | 0.312149 | 0.846344 | 82.018% |
| 2 | 0 | 173357.8 | 29.116% | 2.679311 | 67.935% | 0.069363 | 1.093802 | 0.349403 | 0.830498 | 79.023% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
