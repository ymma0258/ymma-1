# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.476596 | 0.000% | 0.298159 | 3.078851 | 0.207560 | 0.876672 | 89.828% |
| 1 | 0 | 177082.0 | 20.685% | 3.842953 | 59.448% | 0.080490 | 1.541615 | 0.316236 | 0.815860 | 79.015% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
