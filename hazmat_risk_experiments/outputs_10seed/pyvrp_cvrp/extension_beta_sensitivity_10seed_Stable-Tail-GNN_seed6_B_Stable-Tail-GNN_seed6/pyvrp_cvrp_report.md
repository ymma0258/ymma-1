# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.958100 | 0.000% | 0.279888 | 2.949124 | 0.219800 | 0.881360 | 90.236% |
| 0.5 | 0 | 167815.2 | 14.369% | 5.559252 | 37.942% | 0.141444 | 1.928095 | 0.300481 | 0.863391 | 86.076% |
| 1 | 0 | 180433.6 | 22.969% | 4.036839 | 54.936% | 0.094482 | 1.501284 | 0.313530 | 0.838460 | 81.424% |
| 1.5 | 0 | 190458.3 | 29.801% | 3.511972 | 60.796% | 0.084823 | 1.417336 | 0.339905 | 0.827449 | 79.405% |
| 2 | 0 | 200084.0 | 36.361% | 3.336244 | 62.757% | 0.082163 | 1.374694 | 0.359027 | 0.823399 | 78.559% |
| 3 | 0 | 218709.5 | 49.055% | 3.313869 | 63.007% | 0.081285 | 1.377468 | 0.364401 | 0.821471 | 78.304% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
