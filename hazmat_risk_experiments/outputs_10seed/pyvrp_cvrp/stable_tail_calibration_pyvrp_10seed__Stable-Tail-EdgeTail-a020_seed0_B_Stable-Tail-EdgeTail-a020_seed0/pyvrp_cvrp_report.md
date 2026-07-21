# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.724043 | 0.000% | 0.212313 | 2.632680 | 0.257289 | 0.880524 | 89.769% |
| 0.25 | 0 | 156590.3 | 6.574% | 6.368021 | 17.556% | 0.153638 | 2.425338 | 0.279388 | 0.871145 | 88.247% |
| 0.5 | 0 | 164648.0 | 12.058% | 4.348670 | 43.700% | 0.110096 | 1.424689 | 0.216464 | 0.846606 | 83.996% |
| 1 | 0 | 175024.5 | 19.121% | 3.112119 | 59.709% | 0.078744 | 1.070840 | 0.258231 | 0.807735 | 77.941% |
| 2 | 0 | 189668.1 | 29.087% | 2.432167 | 68.512% | 0.050429 | 0.853845 | 0.268935 | 0.778132 | 72.522% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
