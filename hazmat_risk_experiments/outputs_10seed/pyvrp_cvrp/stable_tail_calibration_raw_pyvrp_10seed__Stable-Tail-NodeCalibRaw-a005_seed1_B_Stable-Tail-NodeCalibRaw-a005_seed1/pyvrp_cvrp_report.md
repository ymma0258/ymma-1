# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147396.9 | 0.000% | 9.907000 | 0.000% | 0.314391 | 3.495658 | 0.269823 | 0.872601 | 89.952% |
| 0.25 | 0 | 156078.6 | 5.890% | 7.641234 | 22.870% | 0.209198 | 2.393026 | 0.226080 | 0.866613 | 88.185% |
| 0.5 | 0 | 164557.6 | 11.643% | 6.525243 | 34.135% | 0.162948 | 2.273492 | 0.271625 | 0.857107 | 86.616% |
| 1 | 0 | 174474.6 | 18.371% | 3.777281 | 61.873% | 0.081994 | 1.272368 | 0.282559 | 0.811914 | 78.629% |
| 2 | 0 | 188782.0 | 28.077% | 3.389815 | 65.784% | 0.069952 | 1.160327 | 0.272033 | 0.800014 | 76.463% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
