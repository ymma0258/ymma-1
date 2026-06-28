# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 11.209976 | 0.000% | 0.218857 | 3.261874 | 0.150353 | 0.874139 | 89.971% |
| 1 | 0 | 160760.2 | 19.973% | 4.356459 | 61.138% | 0.062967 | 1.561184 | 0.319446 | 0.806258 | 78.320% |
| 2 | 0 | 175214.8 | 30.760% | 3.133806 | 72.044% | 0.042112 | 1.305614 | 0.354549 | 0.748822 | 70.110% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
