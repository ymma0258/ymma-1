# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.089839 | 0.000% | 0.216892 | 2.417845 | 0.251143 | 0.871207 | 89.130% |
| 0.25 | 0 | 155132.7 | 5.582% | 5.940527 | 16.211% | 0.146596 | 2.159521 | 0.285473 | 0.865254 | 88.191% |
| 0.5 | 0 | 162925.8 | 10.886% | 4.419661 | 37.662% | 0.113261 | 1.670902 | 0.285835 | 0.851403 | 85.125% |
| 1 | 0 | 174632.7 | 18.854% | 3.522816 | 50.312% | 0.089323 | 1.436896 | 0.308518 | 0.836210 | 82.080% |
| 2 | 0 | 191486.3 | 30.324% | 2.692646 | 62.021% | 0.067345 | 1.110088 | 0.297363 | 0.806221 | 77.062% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
