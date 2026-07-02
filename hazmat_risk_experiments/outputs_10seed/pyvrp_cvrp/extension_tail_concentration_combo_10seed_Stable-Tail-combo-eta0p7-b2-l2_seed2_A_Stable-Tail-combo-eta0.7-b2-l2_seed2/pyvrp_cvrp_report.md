# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.698255 | 0.000% | 0.272341 | 2.457055 | 0.145302 | 0.877596 | 90.238% |
| 2 | 2 | 198756.6 | 48.328% | 2.660609 | 69.412% | 0.057077 | 1.593982 | 0.455135 | 0.785725 | 73.410% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
