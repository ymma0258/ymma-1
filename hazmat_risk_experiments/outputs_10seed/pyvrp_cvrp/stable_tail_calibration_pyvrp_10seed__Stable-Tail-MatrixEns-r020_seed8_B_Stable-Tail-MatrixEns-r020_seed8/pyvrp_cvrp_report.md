# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 6.072185 | 0.000% | 0.187143 | 1.851674 | 0.190430 | 0.860631 | 87.817% |
| 0.25 | 0 | 156355.8 | 6.366% | 4.805773 | 20.856% | 0.112777 | 1.575731 | 0.215880 | 0.853436 | 86.365% |
| 0.5 | 0 | 164916.7 | 12.190% | 3.847460 | 36.638% | 0.096383 | 1.278133 | 0.229867 | 0.836900 | 83.681% |
| 1 | 0 | 175724.7 | 19.543% | 2.466020 | 59.388% | 0.059007 | 0.875528 | 0.254266 | 0.783008 | 75.544% |
| 2 | 0 | 189998.1 | 29.253% | 1.950762 | 67.874% | 0.041759 | 0.545869 | 0.195470 | 0.751355 | 70.511% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
