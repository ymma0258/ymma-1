# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.2 | 0.000% | 8.952553 | 0.000% | 0.255828 | 3.002362 | 0.234418 | 0.867931 | 89.055% |
| 0.25 | 0 | 158263.7 | 7.421% | 7.605560 | 15.046% | 0.191089 | 2.399827 | 0.213768 | 0.868668 | 89.025% |
| 0.5 | 0 | 168432.6 | 14.323% | 6.506504 | 27.322% | 0.165312 | 2.292354 | 0.268914 | 0.859102 | 87.107% |
| 1 | 0 | 181936.7 | 23.489% | 4.222467 | 52.835% | 0.109857 | 1.495356 | 0.295094 | 0.827003 | 81.219% |
| 2 | 0 | 203477.3 | 38.110% | 3.759237 | 58.009% | 0.095947 | 1.304345 | 0.308223 | 0.816181 | 79.123% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
