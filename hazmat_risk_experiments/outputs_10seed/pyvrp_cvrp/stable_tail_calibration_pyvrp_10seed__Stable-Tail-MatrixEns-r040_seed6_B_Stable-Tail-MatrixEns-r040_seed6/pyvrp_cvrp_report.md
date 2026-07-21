# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 5.435804 | 0.000% | 0.168490 | 1.768508 | 0.216798 | 0.870246 | 89.246% |
| 0.25 | 0 | 157375.0 | 7.157% | 4.726775 | 13.044% | 0.116598 | 1.528302 | 0.228680 | 0.869477 | 89.403% |
| 0.5 | 0 | 168097.6 | 14.458% | 3.724367 | 31.485% | 0.094856 | 1.365935 | 0.277241 | 0.857576 | 86.788% |
| 1 | 0 | 180940.9 | 23.203% | 2.580535 | 52.527% | 0.064216 | 1.002099 | 0.339487 | 0.828812 | 81.603% |
| 2 | 0 | 201146.2 | 36.961% | 2.232434 | 58.931% | 0.056654 | 0.882268 | 0.359523 | 0.817558 | 79.336% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
