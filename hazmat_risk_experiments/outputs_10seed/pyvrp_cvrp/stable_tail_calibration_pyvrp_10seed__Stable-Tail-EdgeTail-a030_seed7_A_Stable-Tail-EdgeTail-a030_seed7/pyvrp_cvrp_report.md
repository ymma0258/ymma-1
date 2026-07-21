# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 9.226251 | 0.000% | 0.304676 | 2.643294 | 0.169899 | 0.874984 | 89.754% |
| 0.25 | 0 | 143130.2 | 6.815% | 5.803173 | 37.102% | 0.174227 | 1.807580 | 0.223168 | 0.857370 | 86.391% |
| 0.5 | 0 | 149200.8 | 11.346% | 4.662255 | 49.468% | 0.136963 | 1.862296 | 0.303476 | 0.836870 | 83.393% |
| 1 | 0 | 158592.3 | 18.354% | 3.179237 | 65.541% | 0.085987 | 1.375905 | 0.311065 | 0.795442 | 76.673% |
| 2 | 0 | 171413.3 | 27.922% | 2.587844 | 71.951% | 0.061419 | 0.838012 | 0.255565 | 0.763333 | 71.668% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
