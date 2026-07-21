# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.4 | 0.000% | 7.640536 | 0.000% | 0.217250 | 2.296199 | 0.191237 | 0.860239 | 87.736% |
| 0.25 | 0 | 156483.2 | 6.357% | 6.248852 | 18.214% | 0.148729 | 2.160854 | 0.219352 | 0.853813 | 86.734% |
| 0.5 | 0 | 164907.0 | 12.082% | 5.013606 | 34.381% | 0.126061 | 1.485638 | 0.193871 | 0.842229 | 84.174% |
| 1 | 0 | 175821.0 | 19.500% | 3.278452 | 57.091% | 0.078744 | 1.184351 | 0.268491 | 0.792223 | 76.982% |
| 2 | 0 | 190884.8 | 29.739% | 2.561749 | 66.472% | 0.051206 | 0.751594 | 0.186427 | 0.758286 | 71.584% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
