# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.8 | 0.000% | 8.530095 | 0.000% | 0.255441 | 2.504062 | 0.167101 | 0.872168 | 89.215% |
| 0.25 | 0 | 143214.9 | 6.560% | 5.508252 | 35.426% | 0.161067 | 1.984012 | 0.281888 | 0.853579 | 86.305% |
| 0.5 | 0 | 149028.6 | 10.886% | 4.346451 | 49.046% | 0.127780 | 1.647248 | 0.319898 | 0.829998 | 83.167% |
| 1 | 0 | 158328.6 | 17.806% | 2.996710 | 64.869% | 0.080136 | 0.978390 | 0.266438 | 0.782033 | 76.315% |
| 2 | 0 | 171703.5 | 27.758% | 2.306918 | 72.956% | 0.053665 | 0.856611 | 0.315786 | 0.733909 | 69.750% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
