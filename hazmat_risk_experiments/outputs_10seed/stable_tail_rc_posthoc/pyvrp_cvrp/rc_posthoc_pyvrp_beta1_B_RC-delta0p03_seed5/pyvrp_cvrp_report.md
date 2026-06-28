# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.043991 | 0.000% | 0.213982 | 2.344311 | 0.223071 | 0.875576 | 89.322% |
| 1 | 0 | 174685.4 | 18.890% | 2.976812 | 57.740% | 0.068048 | 1.175140 | 0.329666 | 0.809976 | 78.187% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
