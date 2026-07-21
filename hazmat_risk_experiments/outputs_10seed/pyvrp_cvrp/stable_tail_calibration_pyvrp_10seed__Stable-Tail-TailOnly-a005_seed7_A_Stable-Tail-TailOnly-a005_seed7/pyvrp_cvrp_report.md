# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.1 | 0.000% | 9.045637 | 0.000% | 0.291322 | 2.588717 | 0.185035 | 0.874784 | 89.331% |
| 0.25 | 0 | 143421.2 | 6.873% | 5.927398 | 34.472% | 0.173926 | 1.889259 | 0.218865 | 0.857488 | 86.498% |
| 0.5 | 0 | 149460.4 | 11.373% | 4.552792 | 49.669% | 0.131505 | 1.838874 | 0.300457 | 0.833546 | 83.047% |
| 1 | 0 | 159038.8 | 18.510% | 3.305437 | 63.458% | 0.088921 | 1.314241 | 0.299674 | 0.795552 | 77.056% |
| 2 | 0 | 171787.1 | 28.010% | 2.603668 | 71.216% | 0.062084 | 0.914939 | 0.274270 | 0.764108 | 71.685% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
