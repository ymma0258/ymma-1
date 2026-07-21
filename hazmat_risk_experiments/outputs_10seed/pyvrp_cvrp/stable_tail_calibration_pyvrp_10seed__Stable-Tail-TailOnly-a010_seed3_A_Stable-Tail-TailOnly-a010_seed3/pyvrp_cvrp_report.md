# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 7.379754 | 0.000% | 0.227306 | 2.557105 | 0.222929 | 0.877944 | 89.344% |
| 0.25 | 0 | 141760.1 | 5.530% | 5.159890 | 30.080% | 0.147315 | 1.566542 | 0.191251 | 0.860810 | 87.415% |
| 0.5 | 0 | 147218.5 | 9.594% | 3.647051 | 50.580% | 0.103965 | 1.250529 | 0.225447 | 0.833155 | 83.022% |
| 1 | 0 | 154894.7 | 15.308% | 2.530993 | 65.704% | 0.067116 | 0.801577 | 0.231674 | 0.781582 | 75.875% |
| 2 | 0 | 166213.6 | 23.734% | 2.183479 | 70.413% | 0.053279 | 0.689137 | 0.237397 | 0.754295 | 71.994% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
