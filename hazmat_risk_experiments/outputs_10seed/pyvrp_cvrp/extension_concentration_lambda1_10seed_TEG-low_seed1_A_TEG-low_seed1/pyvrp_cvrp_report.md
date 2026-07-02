# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.724775 | 0.000% | 0.250250 | 2.378467 | 0.168382 | 0.839684 | 86.435% |
| 1 | 0 | 157339.9 | 17.420% | 2.927855 | 62.098% | 0.060614 | 0.944578 | 0.237263 | 0.692886 | 68.258% |
| 1 | 1 | 166147.4 | 23.993% | 2.295262 | 70.287% | 0.042978 | 0.715552 | 0.184859 | 0.619824 | 59.359% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
