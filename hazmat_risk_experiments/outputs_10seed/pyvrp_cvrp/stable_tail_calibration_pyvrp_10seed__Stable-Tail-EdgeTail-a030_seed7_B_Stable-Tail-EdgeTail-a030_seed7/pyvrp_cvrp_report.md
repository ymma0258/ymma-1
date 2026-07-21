# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 10.337307 | 0.000% | 0.314097 | 3.150939 | 0.188286 | 0.880815 | 90.865% |
| 0.25 | 0 | 158067.3 | 7.531% | 8.314913 | 19.564% | 0.239229 | 2.698702 | 0.217668 | 0.877526 | 89.703% |
| 0.5 | 0 | 167217.1 | 13.755% | 5.818724 | 43.711% | 0.158289 | 2.051123 | 0.266182 | 0.854447 | 85.499% |
| 1 | 0 | 178597.5 | 21.497% | 3.929707 | 61.985% | 0.101885 | 1.368141 | 0.270876 | 0.828150 | 80.248% |
| 2 | 0 | 195222.1 | 32.807% | 3.455519 | 66.572% | 0.082747 | 1.067721 | 0.209382 | 0.813541 | 77.899% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
