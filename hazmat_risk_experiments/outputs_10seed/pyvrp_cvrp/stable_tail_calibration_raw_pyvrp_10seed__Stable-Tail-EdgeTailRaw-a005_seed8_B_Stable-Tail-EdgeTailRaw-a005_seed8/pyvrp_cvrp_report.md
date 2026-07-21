# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 7.360363 | 0.000% | 0.214308 | 2.311807 | 0.202703 | 0.857220 | 87.387% |
| 0.25 | 0 | 156988.8 | 6.604% | 6.324441 | 14.074% | 0.146998 | 1.996304 | 0.196463 | 0.854963 | 86.982% |
| 0.5 | 0 | 165240.8 | 12.207% | 5.125663 | 30.361% | 0.124818 | 1.703577 | 0.225542 | 0.843243 | 84.528% |
| 1 | 0 | 176186.0 | 19.640% | 3.102641 | 57.847% | 0.073750 | 1.069330 | 0.220696 | 0.788698 | 76.207% |
| 2 | 0 | 191373.5 | 29.953% | 2.478161 | 66.331% | 0.052866 | 0.699459 | 0.194246 | 0.754256 | 70.813% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
