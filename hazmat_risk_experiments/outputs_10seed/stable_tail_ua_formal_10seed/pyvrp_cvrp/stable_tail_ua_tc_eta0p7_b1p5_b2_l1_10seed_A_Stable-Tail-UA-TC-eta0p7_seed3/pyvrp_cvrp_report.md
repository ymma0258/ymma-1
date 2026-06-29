# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 10.257497 | 0.000% | 0.251596 | 2.971286 | 0.156540 | 0.853713 | 88.441% |
| 1.5 | 1 | 180186.3 | 34.470% | 2.903301 | 71.696% | 0.050092 | 0.927801 | 0.272123 | 0.675072 | 64.808% |
| 2 | 1 | 186466.0 | 39.156% | 2.716137 | 73.520% | 0.045000 | 1.115670 | 0.326852 | 0.651664 | 62.120% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
