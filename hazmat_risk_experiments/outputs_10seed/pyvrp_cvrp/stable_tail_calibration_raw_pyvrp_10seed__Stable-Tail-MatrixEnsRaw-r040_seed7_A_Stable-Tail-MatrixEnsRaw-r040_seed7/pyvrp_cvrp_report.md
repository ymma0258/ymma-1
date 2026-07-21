# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 5.456104 | 0.000% | 0.177485 | 1.555527 | 0.171985 | 0.875533 | 89.805% |
| 0.25 | 0 | 143081.1 | 6.725% | 3.567343 | 34.617% | 0.107327 | 1.138325 | 0.233941 | 0.861594 | 86.916% |
| 0.5 | 0 | 149267.0 | 11.340% | 2.791267 | 48.841% | 0.079607 | 1.037961 | 0.256467 | 0.838006 | 83.380% |
| 1 | 0 | 158165.3 | 17.977% | 2.007715 | 63.202% | 0.055379 | 0.814687 | 0.305791 | 0.799768 | 77.525% |
| 2 | 0 | 171348.6 | 27.810% | 1.580334 | 71.035% | 0.037032 | 0.512799 | 0.235114 | 0.766678 | 72.242% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
