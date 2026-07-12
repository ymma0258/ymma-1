# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 9.611096 | 0.000% | 0.314054 | 2.827452 | 0.166177 | 0.845755 | 87.323% |
| 0.25 | 0 | 143332.9 | 6.701% | 6.258517 | 34.882% | 0.156109 | 2.044933 | 0.228593 | 0.822025 | 84.382% |
| 0.5 | 0 | 150192.0 | 11.807% | 5.078993 | 47.155% | 0.132629 | 1.699343 | 0.230299 | 0.799609 | 81.044% |
| 1 | 0 | 160524.3 | 19.499% | 3.566114 | 62.896% | 0.079502 | 1.234473 | 0.307608 | 0.736547 | 72.911% |
| 2 | 0 | 177057.7 | 31.807% | 3.390281 | 64.725% | 0.068031 | 1.123827 | 0.285584 | 0.724469 | 71.415% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
