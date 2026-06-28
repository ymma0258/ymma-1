# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 11.804737 | 0.000% | 0.300314 | 3.657283 | 0.192179 | 0.853547 | 88.510% |
| 1.5 | 1 | 210830.1 | 43.685% | 4.125181 | 65.055% | 0.075086 | 1.428014 | 0.255826 | 0.744753 | 72.918% |
| 2 | 1 | 220204.3 | 50.074% | 4.139582 | 64.933% | 0.075053 | 1.590011 | 0.353062 | 0.746251 | 72.967% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
