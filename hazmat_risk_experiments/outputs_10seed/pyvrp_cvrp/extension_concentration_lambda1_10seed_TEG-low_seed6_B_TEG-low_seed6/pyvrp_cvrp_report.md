# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.724288 | 0.000% | 0.259268 | 2.812094 | 0.210690 | 0.844702 | 87.212% |
| 1 | 0 | 180103.9 | 22.744% | 4.386909 | 49.716% | 0.091800 | 1.457833 | 0.285867 | 0.773276 | 76.681% |
| 1 | 1 | 195421.7 | 33.184% | 3.563117 | 59.159% | 0.068664 | 1.336047 | 0.289042 | 0.736167 | 71.516% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
