# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134065.0 | 0.000% | 8.440500 | 0.000% | 0.279073 | 2.522833 | 0.175741 | 0.875843 | 89.469% |
| 0.25 | 0 | 142485.8 | 6.281% | 5.527224 | 34.515% | 0.161584 | 1.935645 | 0.268085 | 0.865209 | 87.554% |
| 0.5 | 0 | 148564.9 | 10.816% | 4.528522 | 46.348% | 0.133413 | 1.705981 | 0.262217 | 0.852298 | 85.438% |
| 1 | 0 | 157983.0 | 17.841% | 3.137132 | 62.832% | 0.086470 | 1.097900 | 0.255261 | 0.811423 | 79.117% |
| 2 | 0 | 171815.5 | 28.158% | 2.636079 | 68.769% | 0.061721 | 1.082975 | 0.355332 | 0.790321 | 75.616% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
