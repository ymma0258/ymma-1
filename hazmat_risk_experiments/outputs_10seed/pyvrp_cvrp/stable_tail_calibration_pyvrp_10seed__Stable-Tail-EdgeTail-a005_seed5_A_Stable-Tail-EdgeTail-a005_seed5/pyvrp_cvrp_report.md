# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.5 | 0.000% | 7.315590 | 0.000% | 0.226016 | 2.180984 | 0.184637 | 0.871437 | 88.607% |
| 0.25 | 0 | 142295.0 | 6.086% | 4.910310 | 32.879% | 0.137480 | 1.522339 | 0.224064 | 0.858856 | 85.981% |
| 0.5 | 0 | 147788.7 | 10.182% | 3.732379 | 48.980% | 0.110102 | 1.442822 | 0.306761 | 0.829156 | 82.068% |
| 1 | 0 | 155965.0 | 16.278% | 2.438798 | 66.663% | 0.062169 | 0.941282 | 0.292623 | 0.768976 | 73.113% |
| 2 | 0 | 167764.8 | 25.075% | 1.978476 | 72.955% | 0.044049 | 0.619935 | 0.221987 | 0.725928 | 66.998% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
