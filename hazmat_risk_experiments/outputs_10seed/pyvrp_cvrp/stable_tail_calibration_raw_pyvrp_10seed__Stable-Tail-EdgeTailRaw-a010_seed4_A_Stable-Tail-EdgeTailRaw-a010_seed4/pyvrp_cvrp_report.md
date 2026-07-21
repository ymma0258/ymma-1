# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.0 | 0.000% | 8.806227 | 0.000% | 0.276573 | 2.617421 | 0.165110 | 0.878456 | 89.992% |
| 0.25 | 0 | 143198.2 | 6.707% | 7.072630 | 19.686% | 0.225615 | 2.182741 | 0.239479 | 0.876432 | 89.433% |
| 0.5 | 0 | 150116.8 | 11.862% | 5.230304 | 40.607% | 0.161139 | 1.897277 | 0.278522 | 0.857967 | 86.398% |
| 1 | 0 | 159694.3 | 18.999% | 3.706114 | 57.915% | 0.096200 | 1.180680 | 0.255987 | 0.821913 | 80.909% |
| 2 | 0 | 174674.8 | 30.162% | 2.853093 | 67.601% | 0.065471 | 1.054109 | 0.336889 | 0.789592 | 75.799% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
