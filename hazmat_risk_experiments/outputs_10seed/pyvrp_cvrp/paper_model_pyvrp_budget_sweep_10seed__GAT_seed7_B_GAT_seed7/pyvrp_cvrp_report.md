# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.3 | 0.000% | 9.560311 | 0.000% | 0.292896 | 3.324380 | 0.247839 | 0.857233 | 89.762% |
| 0.25 | 0 | 157074.1 | 6.710% | 8.492442 | 11.170% | 0.240635 | 2.712424 | 0.220863 | 0.858100 | 89.239% |
| 0.5 | 0 | 166301.6 | 12.979% | 7.143569 | 25.279% | 0.196670 | 2.361143 | 0.234849 | 0.852638 | 87.500% |
| 1 | 0 | 180696.3 | 22.758% | 5.426485 | 43.239% | 0.145553 | 2.066227 | 0.307353 | 0.836845 | 84.344% |
| 2 | 0 | 203274.1 | 38.096% | 4.676218 | 51.087% | 0.116867 | 1.527564 | 0.272909 | 0.826550 | 82.140% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
