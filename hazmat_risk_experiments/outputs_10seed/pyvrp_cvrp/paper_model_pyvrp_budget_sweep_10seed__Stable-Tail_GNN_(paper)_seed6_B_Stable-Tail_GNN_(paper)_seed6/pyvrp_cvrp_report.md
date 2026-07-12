# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.1 | 0.000% | 8.688473 | 0.000% | 0.254209 | 2.985723 | 0.236385 | 0.866497 | 88.987% |
| 0.25 | 0 | 158321.4 | 7.508% | 7.744387 | 10.866% | 0.202092 | 2.792742 | 0.266423 | 0.867846 | 89.115% |
| 0.5 | 0 | 168836.1 | 14.649% | 6.481846 | 25.397% | 0.163091 | 2.316918 | 0.263584 | 0.858451 | 87.136% |
| 1 | 0 | 182119.1 | 23.668% | 4.194695 | 51.721% | 0.106685 | 1.657428 | 0.342238 | 0.826717 | 81.250% |
| 2 | 0 | 203843.6 | 38.420% | 3.724876 | 57.129% | 0.092516 | 1.433403 | 0.353868 | 0.817150 | 79.248% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
