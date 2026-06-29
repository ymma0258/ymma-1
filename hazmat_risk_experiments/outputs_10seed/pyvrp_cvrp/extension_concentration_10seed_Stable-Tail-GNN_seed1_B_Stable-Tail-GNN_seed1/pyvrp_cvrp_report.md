# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.357164 | 0.000% | 0.239110 | 2.944828 | 0.274723 | 0.883600 | 90.215% |
| 1 | 0 | 173258.1 | 18.079% | 3.125534 | 62.601% | 0.066100 | 1.082979 | 0.274297 | 0.813934 | 77.109% |
| 1 | 0.5 | 178769.8 | 21.835% | 2.727792 | 67.360% | 0.053085 | 1.036782 | 0.313879 | 0.800560 | 74.844% |
| 1 | 1 | 184059.0 | 25.440% | 2.732395 | 67.305% | 0.053025 | 1.028201 | 0.286984 | 0.800218 | 74.707% |
| 1 | 2 | 193972.2 | 32.196% | 2.510368 | 69.961% | 0.048436 | 1.020156 | 0.319018 | 0.792281 | 73.332% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
