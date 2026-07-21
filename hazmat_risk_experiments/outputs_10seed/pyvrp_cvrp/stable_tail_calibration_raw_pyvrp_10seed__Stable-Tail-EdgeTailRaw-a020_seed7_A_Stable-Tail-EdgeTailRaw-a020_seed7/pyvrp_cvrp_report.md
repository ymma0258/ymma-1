# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.2 | 0.000% | 9.307823 | 0.000% | 0.307302 | 2.644063 | 0.158704 | 0.875167 | 89.463% |
| 0.25 | 0 | 143430.7 | 6.774% | 5.736495 | 38.369% | 0.170243 | 1.849895 | 0.233625 | 0.856429 | 86.315% |
| 0.5 | 0 | 149160.6 | 11.039% | 4.669309 | 49.835% | 0.135400 | 1.721347 | 0.292991 | 0.836983 | 83.331% |
| 1 | 0 | 158689.8 | 18.133% | 3.297699 | 64.571% | 0.088315 | 1.178011 | 0.294600 | 0.800263 | 77.376% |
| 2 | 0 | 171664.5 | 27.792% | 2.661317 | 71.408% | 0.062415 | 0.832573 | 0.228139 | 0.766006 | 72.100% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
