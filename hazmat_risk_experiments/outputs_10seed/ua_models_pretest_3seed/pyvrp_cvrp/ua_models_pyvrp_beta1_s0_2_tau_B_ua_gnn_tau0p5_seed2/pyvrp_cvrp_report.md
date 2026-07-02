# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 14.664467 | 0.000% | 0.234445 | 4.732076 | 0.213661 | 0.841052 | 89.315% |
| 1 | 0 | 185103.7 | 26.592% | 8.509615 | 41.971% | 0.150783 | 3.069283 | 0.256356 | 0.805654 | 83.005% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
