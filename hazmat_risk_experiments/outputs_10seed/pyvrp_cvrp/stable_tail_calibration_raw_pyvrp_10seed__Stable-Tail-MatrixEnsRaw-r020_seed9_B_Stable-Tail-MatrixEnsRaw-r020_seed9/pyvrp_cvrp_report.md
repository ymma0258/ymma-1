# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.4 | 0.000% | 7.228886 | 0.000% | 0.229370 | 2.227762 | 0.194936 | 0.871080 | 90.017% |
| 0.25 | 0 | 158349.1 | 7.625% | 6.230293 | 13.814% | 0.187742 | 1.964341 | 0.217421 | 0.871155 | 89.588% |
| 0.5 | 0 | 168067.6 | 14.230% | 4.014309 | 44.468% | 0.107456 | 1.420933 | 0.274365 | 0.843036 | 84.800% |
| 1 | 0 | 179425.1 | 21.950% | 2.865378 | 60.362% | 0.065820 | 0.973053 | 0.273826 | 0.816221 | 79.627% |
| 2 | 0 | 196422.0 | 33.502% | 2.467019 | 65.873% | 0.050717 | 0.806496 | 0.257465 | 0.795741 | 76.733% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
