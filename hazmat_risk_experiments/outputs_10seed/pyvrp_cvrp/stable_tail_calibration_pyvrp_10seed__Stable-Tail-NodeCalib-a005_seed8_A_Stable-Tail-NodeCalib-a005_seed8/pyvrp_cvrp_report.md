# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 7.893899 | 0.000% | 0.247658 | 2.400939 | 0.183405 | 0.870277 | 88.846% |
| 0.25 | 0 | 143245.4 | 6.795% | 5.025747 | 36.334% | 0.150497 | 1.598962 | 0.216799 | 0.853686 | 86.002% |
| 0.5 | 0 | 149788.4 | 11.673% | 3.963506 | 49.790% | 0.114684 | 1.502633 | 0.259192 | 0.825434 | 82.143% |
| 1 | 0 | 158835.0 | 18.417% | 2.782378 | 64.753% | 0.070649 | 0.862702 | 0.193589 | 0.779364 | 75.345% |
| 2 | 0 | 173970.2 | 29.701% | 2.163243 | 72.596% | 0.041576 | 0.665456 | 0.201502 | 0.739201 | 68.948% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
