# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.448016 | 0.000% | 0.211877 | 2.245118 | 0.178909 | 0.876900 | 88.876% |
| 1 | 0 | 175801.1 | 19.649% | 3.258818 | 56.246% | 0.082834 | 1.314298 | 0.309727 | 0.817357 | 78.743% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
