# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.958100 | 0.000% | 0.279888 | 2.949124 | 0.219800 | 0.881360 | 90.236% |
| 1 | 0 | 180433.6 | 22.969% | 4.036839 | 54.936% | 0.094482 | 1.501284 | 0.313530 | 0.838460 | 81.424% |
| 1 | 1 | 196961.0 | 34.233% | 3.387683 | 62.183% | 0.083324 | 1.359792 | 0.357126 | 0.825646 | 78.874% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
