# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 9.315896 | 0.000% | 0.295306 | 2.654632 | 0.168924 | 0.879947 | 90.388% |
| 0.25 | 0 | 143349.9 | 6.714% | 7.030744 | 24.530% | 0.219784 | 2.256801 | 0.234930 | 0.876352 | 89.290% |
| 0.5 | 0 | 150065.6 | 11.713% | 5.126852 | 44.967% | 0.155457 | 1.513473 | 0.215096 | 0.854993 | 85.862% |
| 1 | 0 | 159582.0 | 18.797% | 3.722627 | 60.040% | 0.099395 | 1.283323 | 0.289464 | 0.825081 | 81.149% |
| 2 | 0 | 174406.6 | 29.833% | 2.932635 | 68.520% | 0.071220 | 1.119314 | 0.333802 | 0.794121 | 76.331% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
