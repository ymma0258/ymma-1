# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.2 | 0.000% | 8.922528 | 0.000% | 0.276141 | 2.877016 | 0.216518 | 0.876205 | 89.604% |
| 0.25 | 0 | 156526.0 | 6.193% | 7.563322 | 15.233% | 0.207324 | 2.289644 | 0.195142 | 0.873633 | 88.699% |
| 0.5 | 0 | 164555.4 | 11.641% | 5.704243 | 36.069% | 0.152251 | 1.859271 | 0.235771 | 0.857216 | 85.602% |
| 1 | 0 | 174675.4 | 18.507% | 3.846864 | 56.886% | 0.098466 | 1.483415 | 0.307623 | 0.819182 | 79.723% |
| 2 | 0 | 190001.0 | 28.904% | 3.244298 | 63.639% | 0.073173 | 1.364241 | 0.329080 | 0.801332 | 76.984% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
