# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.7 | 0.000% | 10.090055 | 0.000% | 0.329777 | 2.889460 | 0.180497 | 0.879582 | 90.246% |
| 0.25 | 0 | 143101.3 | 6.687% | 7.159282 | 29.046% | 0.215152 | 2.544419 | 0.262475 | 0.873671 | 88.902% |
| 0.5 | 0 | 149216.7 | 11.246% | 5.034193 | 50.107% | 0.150671 | 1.524034 | 0.192258 | 0.848129 | 84.768% |
| 1 | 0 | 158566.3 | 18.217% | 3.624476 | 64.079% | 0.102249 | 1.354090 | 0.315799 | 0.816891 | 79.550% |
| 2 | 0 | 171198.0 | 27.634% | 2.749926 | 72.746% | 0.066553 | 0.944755 | 0.269092 | 0.772768 | 72.934% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
