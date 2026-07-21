# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 5.500515 | 0.000% | 0.174336 | 1.796042 | 0.222007 | 0.873757 | 90.350% |
| 0.25 | 0 | 157886.1 | 7.602% | 4.712850 | 14.320% | 0.129498 | 1.527351 | 0.224969 | 0.871216 | 89.662% |
| 0.5 | 0 | 167213.1 | 13.959% | 2.802835 | 49.044% | 0.077506 | 0.872406 | 0.252000 | 0.840050 | 84.037% |
| 1 | 0 | 178423.0 | 21.599% | 2.002335 | 63.597% | 0.042535 | 0.682315 | 0.252610 | 0.804462 | 78.256% |
| 2 | 0 | 194807.0 | 32.765% | 1.806661 | 67.155% | 0.035188 | 0.574204 | 0.244882 | 0.791353 | 76.160% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
