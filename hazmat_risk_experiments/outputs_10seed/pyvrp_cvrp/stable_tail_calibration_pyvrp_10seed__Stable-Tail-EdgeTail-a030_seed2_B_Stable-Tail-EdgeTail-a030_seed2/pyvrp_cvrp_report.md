# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 9.407860 | 0.000% | 0.294004 | 3.635493 | 0.320344 | 0.880314 | 90.190% |
| 0.25 | 0 | 156344.9 | 6.407% | 7.586525 | 19.360% | 0.232320 | 3.059339 | 0.340392 | 0.874712 | 88.976% |
| 0.5 | 0 | 164582.3 | 12.014% | 6.475454 | 31.170% | 0.184089 | 2.448372 | 0.289996 | 0.865527 | 87.338% |
| 1 | 0 | 176812.7 | 20.338% | 4.592321 | 51.186% | 0.123888 | 1.858113 | 0.304960 | 0.848030 | 83.888% |
| 2 | 0 | 195321.2 | 32.934% | 3.862337 | 58.946% | 0.097747 | 1.745866 | 0.368114 | 0.835885 | 81.354% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
