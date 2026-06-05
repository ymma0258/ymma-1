# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 8.406688 | 0.000% | 0.226655 | 2.752095 | 0.219798 | 0.841198 | 87.350% |
| 1 | 0 | 178489.2 | 21.810% | 3.490541 | 58.479% | 0.070742 | 1.226546 | 0.248276 | 0.712400 | 70.673% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
