# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 8.051215 | 0.000% | 0.261793 | 2.323379 | 0.181040 | 0.884005 | 90.603% |
| 0.25 | 0 | 142194.9 | 5.854% | 5.650512 | 29.818% | 0.158257 | 1.744472 | 0.199077 | 0.880045 | 89.016% |
| 0.5 | 0 | 147910.8 | 10.109% | 4.444751 | 44.794% | 0.131019 | 1.428646 | 0.191758 | 0.871777 | 86.920% |
| 1 | 0 | 156590.2 | 16.570% | 3.177316 | 60.536% | 0.082452 | 0.864553 | 0.150161 | 0.838099 | 81.449% |
| 2 | 0 | 170078.8 | 26.611% | 2.634299 | 67.281% | 0.063826 | 0.960828 | 0.300039 | 0.824127 | 78.431% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
