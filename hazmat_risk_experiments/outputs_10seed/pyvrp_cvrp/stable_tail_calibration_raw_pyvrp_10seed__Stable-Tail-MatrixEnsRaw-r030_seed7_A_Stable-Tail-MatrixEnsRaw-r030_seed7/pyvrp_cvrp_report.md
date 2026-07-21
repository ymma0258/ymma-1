# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 6.468407 | 0.000% | 0.208273 | 1.876178 | 0.191833 | 0.875816 | 89.503% |
| 0.25 | 0 | 143003.8 | 6.562% | 3.920517 | 39.390% | 0.117602 | 1.307692 | 0.238377 | 0.855547 | 86.132% |
| 0.5 | 0 | 149293.1 | 11.248% | 3.274175 | 49.382% | 0.096397 | 1.041417 | 0.196901 | 0.840775 | 83.737% |
| 1 | 0 | 158223.8 | 17.903% | 2.357632 | 63.552% | 0.064439 | 0.896397 | 0.288483 | 0.800710 | 77.647% |
| 2 | 0 | 171169.7 | 27.550% | 1.806277 | 72.075% | 0.042575 | 0.612113 | 0.269381 | 0.760817 | 71.364% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
