# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.679435 | 0.000% | 0.282402 | 2.453869 | 0.143745 | 0.867135 | 89.473% |
| 0.5 | 0 | 149865.4 | 11.842% | 5.228104 | 39.764% | 0.148964 | 1.793445 | 0.232297 | 0.847531 | 85.560% |
| 1 | 0 | 160134.3 | 19.505% | 3.746919 | 56.830% | 0.107632 | 1.234604 | 0.262441 | 0.813504 | 80.309% |
| 1.5 | 0 | 168675.4 | 25.879% | 3.463654 | 60.094% | 0.092379 | 1.121536 | 0.269308 | 0.805976 | 78.913% |
| 2 | 0 | 176598.5 | 31.792% | 3.346144 | 61.447% | 0.086631 | 1.143463 | 0.282838 | 0.797894 | 77.869% |
| 3 | 0 | 190701.2 | 42.317% | 2.727763 | 68.572% | 0.063188 | 1.141528 | 0.355079 | 0.767661 | 73.107% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
