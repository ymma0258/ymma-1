# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 8.012159 | 0.000% | 0.245993 | 2.434329 | 0.183273 | 0.869994 | 88.898% |
| 0.25 | 0 | 143401.7 | 6.805% | 5.559551 | 30.611% | 0.146656 | 1.801003 | 0.239369 | 0.854306 | 86.256% |
| 0.5 | 0 | 149010.9 | 10.983% | 4.107295 | 48.737% | 0.113015 | 1.703637 | 0.314114 | 0.823562 | 82.209% |
| 1 | 0 | 157466.8 | 17.281% | 2.833650 | 64.633% | 0.071340 | 1.095391 | 0.283396 | 0.772180 | 74.522% |
| 2 | 0 | 169041.9 | 25.902% | 2.086432 | 73.959% | 0.042956 | 0.663603 | 0.218717 | 0.707337 | 65.706% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
