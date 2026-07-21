# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.6 | 0.000% | 9.792324 | 0.000% | 0.311201 | 3.372318 | 0.262842 | 0.871927 | 89.860% |
| 0.25 | 0 | 156395.5 | 6.153% | 7.992060 | 18.384% | 0.244795 | 2.860813 | 0.272203 | 0.866757 | 88.574% |
| 0.5 | 0 | 164559.1 | 11.694% | 6.751301 | 31.055% | 0.191616 | 2.043496 | 0.221649 | 0.858503 | 86.737% |
| 1 | 0 | 174327.9 | 18.324% | 3.884650 | 60.330% | 0.085007 | 1.363737 | 0.284321 | 0.816012 | 79.250% |
| 2 | 0 | 188501.5 | 27.945% | 3.294614 | 66.355% | 0.065986 | 1.130213 | 0.260348 | 0.793383 | 75.509% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
