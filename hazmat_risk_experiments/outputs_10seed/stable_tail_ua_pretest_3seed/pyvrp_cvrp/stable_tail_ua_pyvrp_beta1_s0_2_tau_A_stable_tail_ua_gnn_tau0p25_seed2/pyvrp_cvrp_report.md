# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 11.832291 | 0.000% | 0.297241 | 3.207574 | 0.125424 | 0.852151 | 88.817% |
| 1 | 0 | 160962.0 | 20.123% | 4.789258 | 59.524% | 0.088582 | 1.677002 | 0.295119 | 0.784137 | 77.718% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
