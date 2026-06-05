# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 146531.2 | 0.000% | 8.199420 | 0.000% | 0.236188 | 2.653961 | 0.209952 | 0.838219 | 86.846% |
| 0.25 | 157223.6 | 7.297% | 7.246136 | 11.626% | 0.200397 | 2.263326 | 0.207927 | 0.828818 | 85.504% |
| 0.5 | 166700.8 | 13.765% | 5.413317 | 33.979% | 0.125303 | 1.628289 | 0.197629 | 0.792530 | 80.608% |
| 1 | 178390.8 | 21.743% | 3.891981 | 52.533% | 0.076918 | 1.287324 | 0.236042 | 0.724841 | 72.631% |
| 2 | 195474.2 | 33.401% | 2.838472 | 65.382% | 0.052714 | 1.114836 | 0.235565 | 0.653243 | 63.298% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
