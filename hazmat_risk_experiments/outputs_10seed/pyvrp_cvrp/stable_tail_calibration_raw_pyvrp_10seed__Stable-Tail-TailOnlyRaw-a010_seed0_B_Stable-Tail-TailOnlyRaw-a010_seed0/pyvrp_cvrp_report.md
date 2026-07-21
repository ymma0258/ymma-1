# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.5 | 0.000% | 7.686051 | 0.000% | 0.211637 | 2.462824 | 0.225011 | 0.879869 | 89.755% |
| 0.25 | 0 | 156723.0 | 6.520% | 6.479750 | 15.695% | 0.162303 | 2.129282 | 0.245759 | 0.876182 | 88.818% |
| 0.5 | 0 | 165611.5 | 12.561% | 4.760367 | 38.065% | 0.119718 | 1.618783 | 0.243356 | 0.853228 | 84.990% |
| 1 | 0 | 175565.2 | 19.326% | 3.079750 | 59.931% | 0.076274 | 1.179944 | 0.299408 | 0.812187 | 78.281% |
| 2 | 0 | 190807.2 | 29.686% | 2.474859 | 67.801% | 0.052689 | 0.966502 | 0.295864 | 0.782485 | 73.099% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
