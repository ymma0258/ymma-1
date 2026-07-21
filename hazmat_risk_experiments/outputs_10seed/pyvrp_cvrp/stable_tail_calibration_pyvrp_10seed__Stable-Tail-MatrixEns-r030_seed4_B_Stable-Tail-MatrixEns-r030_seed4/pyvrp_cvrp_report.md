# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 5.949404 | 0.000% | 0.179740 | 1.869416 | 0.197350 | 0.873900 | 89.167% |
| 0.25 | 0 | 156108.1 | 6.246% | 5.053529 | 15.058% | 0.134100 | 1.657175 | 0.224235 | 0.871241 | 88.282% |
| 0.5 | 0 | 164708.5 | 12.100% | 3.905827 | 34.349% | 0.106483 | 1.258051 | 0.237213 | 0.854483 | 85.191% |
| 1 | 0 | 175292.0 | 19.303% | 2.655477 | 55.366% | 0.066672 | 1.082298 | 0.334872 | 0.815514 | 79.393% |
| 2 | 0 | 192072.4 | 30.723% | 2.162541 | 63.651% | 0.043493 | 0.822673 | 0.290728 | 0.795429 | 76.077% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
