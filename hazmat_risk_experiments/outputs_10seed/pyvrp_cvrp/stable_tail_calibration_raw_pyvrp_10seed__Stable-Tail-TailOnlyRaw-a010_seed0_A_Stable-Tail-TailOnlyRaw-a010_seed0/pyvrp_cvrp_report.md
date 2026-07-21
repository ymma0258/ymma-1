# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.4 | 0.000% | 7.970704 | 0.000% | 0.237227 | 2.424898 | 0.203862 | 0.884270 | 90.614% |
| 0.25 | 0 | 142384.7 | 6.153% | 4.600919 | 42.277% | 0.139701 | 1.549228 | 0.242037 | 0.862227 | 86.464% |
| 0.5 | 0 | 148161.9 | 10.460% | 3.823575 | 52.030% | 0.109799 | 1.685011 | 0.348290 | 0.844508 | 84.191% |
| 1 | 0 | 155945.8 | 16.263% | 2.432013 | 69.488% | 0.056755 | 1.009669 | 0.293518 | 0.783140 | 75.088% |
| 2 | 0 | 167969.9 | 25.228% | 1.834974 | 76.979% | 0.034628 | 0.560457 | 0.213058 | 0.734490 | 67.077% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
