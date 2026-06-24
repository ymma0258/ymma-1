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
| 1 | 1 | 184086.8 | 25.459% | 2.733863 | 67.287% | 0.053025 | 1.028201 | 0.287117 | 0.799463 | 74.666% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
