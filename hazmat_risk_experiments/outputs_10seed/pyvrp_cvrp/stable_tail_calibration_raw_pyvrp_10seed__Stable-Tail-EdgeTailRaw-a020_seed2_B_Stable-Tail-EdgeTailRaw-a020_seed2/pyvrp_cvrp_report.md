# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147396.7 | 0.000% | 9.141050 | 0.000% | 0.292445 | 3.609090 | 0.328257 | 0.877443 | 89.854% |
| 0.25 | 0 | 156880.2 | 6.434% | 7.880183 | 13.793% | 0.241069 | 3.195730 | 0.331141 | 0.877184 | 89.548% |
| 0.5 | 0 | 165093.5 | 12.006% | 6.441986 | 29.527% | 0.178169 | 2.429315 | 0.277391 | 0.866146 | 87.491% |
| 1 | 0 | 177322.2 | 20.303% | 4.706086 | 48.517% | 0.124640 | 1.932601 | 0.306745 | 0.849421 | 84.204% |
| 2 | 0 | 196114.8 | 33.052% | 3.719629 | 59.309% | 0.093787 | 1.739267 | 0.359160 | 0.828294 | 80.265% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
