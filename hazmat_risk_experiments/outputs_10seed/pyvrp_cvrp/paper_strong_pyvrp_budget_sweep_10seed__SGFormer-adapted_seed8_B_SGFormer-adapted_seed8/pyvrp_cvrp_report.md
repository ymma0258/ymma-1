# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.3 | 0.000% | 6.903296 | 0.000% | 0.201693 | 2.058400 | 0.173412 | 0.873623 | 86.477% |
| 0.25 | 0 | 156084.2 | 5.942% | 5.553370 | 19.555% | 0.157752 | 1.983559 | 0.267061 | 0.862851 | 84.125% |
| 0.5 | 0 | 163300.4 | 10.840% | 3.478683 | 49.608% | 0.079423 | 1.099485 | 0.219792 | 0.804724 | 75.172% |
| 1 | 0 | 171363.6 | 16.313% | 2.556164 | 62.972% | 0.052834 | 0.788762 | 0.199757 | 0.763067 | 67.952% |
| 2 | 0 | 183938.0 | 24.847% | 2.038341 | 70.473% | 0.035951 | 0.650256 | 0.217998 | 0.725429 | 61.260% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
