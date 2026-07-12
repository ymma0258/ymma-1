# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.1 | 0.000% | 9.134487 | 0.000% | 0.265858 | 3.109422 | 0.263404 | 0.883108 | 91.087% |
| 0.25 | 0 | 155319.9 | 5.470% | 7.451884 | 18.420% | 0.204043 | 2.325784 | 0.231745 | 0.882087 | 89.656% |
| 0.5 | 0 | 162713.9 | 10.491% | 6.347664 | 30.509% | 0.185488 | 1.956329 | 0.231263 | 0.878861 | 88.411% |
| 1 | 0 | 172355.6 | 17.038% | 3.555911 | 61.072% | 0.093725 | 1.247461 | 0.274330 | 0.838475 | 81.188% |
| 2 | 0 | 184776.6 | 25.473% | 2.954963 | 67.650% | 0.073796 | 0.990212 | 0.280368 | 0.814893 | 77.047% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
