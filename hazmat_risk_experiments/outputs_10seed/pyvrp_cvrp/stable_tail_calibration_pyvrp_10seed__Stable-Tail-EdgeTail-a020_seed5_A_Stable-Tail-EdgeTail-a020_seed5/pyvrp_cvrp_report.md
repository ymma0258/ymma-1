# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 7.523026 | 0.000% | 0.231004 | 2.207661 | 0.178941 | 0.875223 | 89.139% |
| 0.25 | 0 | 142307.3 | 6.201% | 5.032574 | 33.104% | 0.140149 | 1.587826 | 0.232144 | 0.860087 | 86.336% |
| 0.5 | 0 | 147885.0 | 10.364% | 3.845462 | 48.884% | 0.112438 | 1.552880 | 0.318180 | 0.832720 | 82.551% |
| 1 | 0 | 155619.4 | 16.136% | 2.529983 | 66.370% | 0.065711 | 0.911861 | 0.264353 | 0.774572 | 74.063% |
| 2 | 0 | 166660.8 | 24.375% | 1.803339 | 76.029% | 0.037888 | 0.615915 | 0.255983 | 0.707428 | 64.517% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
