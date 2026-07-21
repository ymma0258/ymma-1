# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 7.151268 | 0.000% | 0.214288 | 2.202693 | 0.185983 | 0.874521 | 89.158% |
| 0.25 | 0 | 141630.6 | 5.591% | 4.805951 | 32.796% | 0.139017 | 1.450222 | 0.191163 | 0.856872 | 86.657% |
| 0.5 | 0 | 147095.7 | 9.665% | 3.855230 | 46.090% | 0.111379 | 1.361650 | 0.255346 | 0.839677 | 84.037% |
| 1 | 0 | 154799.6 | 15.409% | 2.399580 | 66.445% | 0.061951 | 0.742380 | 0.236257 | 0.772477 | 74.378% |
| 2 | 0 | 166796.3 | 24.353% | 2.093980 | 70.719% | 0.050459 | 0.798564 | 0.302158 | 0.747398 | 70.475% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
