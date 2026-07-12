# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 6.430313 | 0.000% | 0.204007 | 2.066733 | 0.227584 | 0.869793 | 88.292% |
| 0.25 | 0 | 140533.4 | 4.565% | 3.694527 | 42.545% | 0.089563 | 1.211689 | 0.219854 | 0.834248 | 81.405% |
| 0.5 | 0 | 144602.9 | 7.593% | 2.800020 | 56.456% | 0.063102 | 0.854078 | 0.147660 | 0.797990 | 76.320% |
| 1 | 0 | 151348.2 | 12.612% | 2.516711 | 60.862% | 0.060603 | 0.805055 | 0.206850 | 0.789703 | 74.385% |
| 2 | 0 | 161087.8 | 19.859% | 1.824492 | 71.627% | 0.040941 | 0.529642 | 0.160363 | 0.731881 | 65.976% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
