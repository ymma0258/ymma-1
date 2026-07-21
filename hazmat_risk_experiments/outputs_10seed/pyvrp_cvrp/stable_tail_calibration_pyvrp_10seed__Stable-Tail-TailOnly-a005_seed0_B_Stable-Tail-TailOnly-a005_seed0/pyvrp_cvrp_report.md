# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.5 | 0.000% | 7.339260 | 0.000% | 0.201550 | 2.525603 | 0.249954 | 0.876436 | 89.221% |
| 0.25 | 0 | 157113.1 | 6.785% | 6.467349 | 11.880% | 0.157989 | 2.204316 | 0.256284 | 0.875024 | 88.709% |
| 0.5 | 0 | 165165.8 | 12.258% | 4.316332 | 41.188% | 0.109045 | 1.459952 | 0.220233 | 0.843322 | 83.544% |
| 1 | 0 | 176149.2 | 19.723% | 2.992489 | 59.226% | 0.074452 | 1.017010 | 0.252789 | 0.805681 | 77.289% |
| 2 | 0 | 190168.8 | 29.252% | 2.454956 | 66.550% | 0.050039 | 0.901030 | 0.272162 | 0.782545 | 73.284% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
