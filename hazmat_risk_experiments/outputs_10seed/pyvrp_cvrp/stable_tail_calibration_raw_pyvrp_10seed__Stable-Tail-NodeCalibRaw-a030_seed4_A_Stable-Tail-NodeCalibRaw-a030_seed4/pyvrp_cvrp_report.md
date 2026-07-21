# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 9.237587 | 0.000% | 0.293358 | 2.662210 | 0.175329 | 0.879922 | 90.271% |
| 0.25 | 0 | 143506.6 | 6.883% | 6.561927 | 28.965% | 0.204951 | 1.903577 | 0.184277 | 0.870167 | 88.468% |
| 0.5 | 0 | 150332.3 | 11.967% | 5.080896 | 44.998% | 0.127114 | 1.618200 | 0.241261 | 0.856858 | 86.039% |
| 1 | 0 | 159999.9 | 19.167% | 3.641486 | 60.580% | 0.086890 | 1.265275 | 0.296126 | 0.819832 | 80.536% |
| 2 | 0 | 175101.3 | 30.415% | 2.913839 | 68.457% | 0.063251 | 1.079694 | 0.335930 | 0.794368 | 76.410% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
