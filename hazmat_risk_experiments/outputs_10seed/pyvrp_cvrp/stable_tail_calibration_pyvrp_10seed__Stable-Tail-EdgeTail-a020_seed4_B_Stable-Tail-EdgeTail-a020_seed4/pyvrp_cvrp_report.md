# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 8.629231 | 0.000% | 0.261132 | 2.729598 | 0.201184 | 0.875176 | 89.333% |
| 0.25 | 0 | 155493.3 | 5.828% | 7.470193 | 13.432% | 0.207965 | 2.559295 | 0.232303 | 0.873354 | 88.669% |
| 0.5 | 0 | 163660.1 | 11.386% | 5.601107 | 35.091% | 0.143264 | 1.951735 | 0.294396 | 0.854887 | 85.291% |
| 1 | 0 | 173856.7 | 18.326% | 3.940351 | 54.337% | 0.100795 | 1.529945 | 0.315838 | 0.822202 | 80.248% |
| 2 | 0 | 189387.2 | 28.896% | 3.336709 | 61.332% | 0.073901 | 1.288119 | 0.300489 | 0.805982 | 77.594% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
