# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 11.833187 | 0.000% | 0.267835 | 3.214132 | 0.131295 | 0.856477 | 89.010% |
| 1.5 | 1 | 185843.7 | 38.692% | 3.675959 | 68.935% | 0.058337 | 1.557289 | 0.363736 | 0.725518 | 69.912% |
| 2 | 1 | 193373.9 | 44.311% | 3.819251 | 67.724% | 0.062951 | 1.558735 | 0.356937 | 0.735894 | 71.125% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
