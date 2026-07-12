# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 7.853148 | 0.000% | 0.207405 | 2.643841 | 0.254752 | 0.856723 | 88.781% |
| 0.25 | 0 | 157762.7 | 7.324% | 6.875659 | 12.447% | 0.172009 | 2.307824 | 0.244847 | 0.853127 | 87.882% |
| 0.5 | 0 | 167579.5 | 14.002% | 5.872275 | 25.224% | 0.159823 | 1.801994 | 0.218039 | 0.846717 | 86.376% |
| 1 | 0 | 182921.7 | 24.439% | 4.448593 | 43.353% | 0.118047 | 1.584887 | 0.307299 | 0.819758 | 82.452% |
| 2 | 0 | 207361.4 | 41.065% | 3.864654 | 50.788% | 0.098629 | 1.438920 | 0.339102 | 0.808026 | 79.967% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
