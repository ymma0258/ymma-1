# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.1 | 0.000% | 4.173167 | 0.000% | 0.121975 | 1.420575 | 0.247473 | 0.870960 | 88.973% |
| 0.25 | 0 | 155309.2 | 5.606% | 3.631091 | 12.990% | 0.092619 | 1.290393 | 0.266356 | 0.867569 | 88.452% |
| 0.5 | 0 | 163034.0 | 10.859% | 2.858893 | 31.493% | 0.072157 | 1.182095 | 0.296775 | 0.855065 | 85.870% |
| 1 | 0 | 174639.8 | 18.751% | 2.178774 | 47.791% | 0.055668 | 0.866778 | 0.297548 | 0.838002 | 82.420% |
| 2 | 0 | 191675.9 | 30.335% | 1.651341 | 60.430% | 0.041046 | 0.683813 | 0.301029 | 0.810763 | 77.765% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
