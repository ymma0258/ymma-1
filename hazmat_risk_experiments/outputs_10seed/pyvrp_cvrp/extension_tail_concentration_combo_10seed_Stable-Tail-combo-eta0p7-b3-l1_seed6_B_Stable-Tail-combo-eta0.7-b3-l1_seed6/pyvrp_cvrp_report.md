# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.958100 | 0.000% | 0.279888 | 2.949124 | 0.219800 | 0.881360 | 90.236% |
| 3 | 1 | 242154.0 | 65.033% | 3.248780 | 63.734% | 0.073646 | 1.402018 | 0.404140 | 0.817166 | 77.452% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
