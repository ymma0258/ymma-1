# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 17.255772 | 0.000% | 0.163271 | 5.193720 | 0.187255 | 0.841710 | 89.498% |
| 1 | 0 | 187015.7 | 27.900% | 10.063832 | 41.678% | 0.101149 | 2.901096 | 0.175191 | 0.811596 | 83.357% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
