# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 6.269608 | 0.000% | 0.188690 | 2.066517 | 0.220109 | 0.869825 | 89.221% |
| 0.25 | 0 | 157613.7 | 7.271% | 5.508453 | 12.140% | 0.135134 | 1.792650 | 0.228124 | 0.868950 | 89.330% |
| 0.5 | 0 | 167720.3 | 14.149% | 4.496875 | 28.275% | 0.117078 | 1.617210 | 0.281241 | 0.860936 | 87.233% |
| 1 | 0 | 180734.9 | 23.007% | 2.929523 | 53.274% | 0.073670 | 1.129463 | 0.355314 | 0.827861 | 81.272% |
| 2 | 0 | 202196.6 | 37.614% | 2.586560 | 58.744% | 0.065329 | 1.021472 | 0.352027 | 0.814677 | 78.804% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
