# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 13.776360 | 0.000% | 0.261130 | 4.536846 | 0.224874 | 0.874862 | 90.928% |
| 1 | 0 | 178599.1 | 21.719% | 5.684368 | 58.738% | 0.074522 | 1.965725 | 0.245605 | 0.843049 | 81.749% |
| 2 | 0 | 196630.7 | 34.008% | 4.852720 | 64.775% | 0.061108 | 1.836724 | 0.339779 | 0.823157 | 78.537% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
