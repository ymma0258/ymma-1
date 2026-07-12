# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 8.740614 | 0.000% | 0.278210 | 2.497919 | 0.165241 | 0.862989 | 88.916% |
| 0.25 | 0 | 143974.0 | 7.231% | 6.112617 | 30.067% | 0.190796 | 2.064444 | 0.227289 | 0.852542 | 87.982% |
| 0.5 | 0 | 151062.4 | 12.511% | 4.755519 | 45.593% | 0.130300 | 1.618547 | 0.233921 | 0.826177 | 84.420% |
| 1 | 0 | 161584.2 | 20.347% | 3.297646 | 62.272% | 0.074642 | 1.212133 | 0.280873 | 0.776860 | 77.505% |
| 2 | 0 | 177480.8 | 32.187% | 2.477530 | 71.655% | 0.050010 | 0.806473 | 0.255989 | 0.721400 | 70.027% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
