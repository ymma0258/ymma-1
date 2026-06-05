# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 7.714395 | 0.000% | 0.232801 | 2.675448 | 0.252838 | 0.859211 | 89.103% |
| 1 | 0 | 179734.0 | 22.659% | 3.561709 | 53.830% | 0.088899 | 1.198548 | 0.293165 | 0.807682 | 79.864% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
