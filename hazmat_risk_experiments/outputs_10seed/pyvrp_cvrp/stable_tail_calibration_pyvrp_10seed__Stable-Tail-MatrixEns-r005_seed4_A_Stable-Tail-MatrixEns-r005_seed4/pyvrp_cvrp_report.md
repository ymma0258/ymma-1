# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 8.186523 | 0.000% | 0.253501 | 2.307108 | 0.152489 | 0.876689 | 89.915% |
| 0.25 | 0 | 143196.1 | 6.864% | 6.329423 | 22.685% | 0.198292 | 1.904560 | 0.205861 | 0.872682 | 88.827% |
| 0.5 | 0 | 150073.1 | 11.996% | 4.672794 | 42.921% | 0.144595 | 1.562538 | 0.263230 | 0.849629 | 85.227% |
| 1 | 0 | 159653.1 | 19.146% | 3.312911 | 59.532% | 0.086169 | 1.371782 | 0.367075 | 0.817599 | 80.198% |
| 2 | 0 | 174564.7 | 30.274% | 2.763327 | 66.245% | 0.066918 | 1.010860 | 0.343551 | 0.793604 | 76.557% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
