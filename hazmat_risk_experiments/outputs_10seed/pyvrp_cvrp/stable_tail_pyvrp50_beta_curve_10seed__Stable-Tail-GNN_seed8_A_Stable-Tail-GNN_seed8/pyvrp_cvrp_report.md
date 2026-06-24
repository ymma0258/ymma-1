# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.481776 | 0.000% | 0.219625 | 2.238807 | 0.159102 | 0.884400 | 90.223% |
| 0.25 | 0 | 142788.2 | 6.560% | 5.778600 | 22.764% | 0.166435 | 1.841240 | 0.257838 | 0.880516 | 88.985% |
| 0.5 | 0 | 148768.7 | 11.023% | 4.103556 | 45.153% | 0.109749 | 1.685447 | 0.321050 | 0.857770 | 85.368% |
| 1 | 0 | 157997.4 | 17.911% | 3.011525 | 59.749% | 0.074084 | 0.869025 | 0.199251 | 0.822900 | 80.016% |
| 2 | 0 | 172268.9 | 28.561% | 2.248659 | 69.945% | 0.047475 | 0.876601 | 0.325153 | 0.787648 | 73.771% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
