# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.484094 | 0.000% | 0.206981 | 2.338143 | 0.178187 | 0.836947 | 86.280% |
| 1 | 0 | 158381.3 | 18.197% | 2.898946 | 61.265% | 0.062244 | 0.931596 | 0.203547 | 0.690020 | 68.425% |
| 1 | 1 | 168423.1 | 25.691% | 2.523950 | 66.276% | 0.047087 | 0.851006 | 0.232564 | 0.655205 | 63.734% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
