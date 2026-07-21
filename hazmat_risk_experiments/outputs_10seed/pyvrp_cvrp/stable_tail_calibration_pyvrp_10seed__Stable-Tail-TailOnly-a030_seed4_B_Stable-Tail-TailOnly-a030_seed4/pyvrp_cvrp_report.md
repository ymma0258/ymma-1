# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 9.083075 | 0.000% | 0.278266 | 2.892707 | 0.203928 | 0.878734 | 89.813% |
| 0.25 | 0 | 155194.3 | 5.672% | 7.831068 | 13.784% | 0.217906 | 2.614613 | 0.238441 | 0.877355 | 89.084% |
| 0.5 | 0 | 162966.2 | 10.964% | 6.168821 | 32.084% | 0.166419 | 1.924611 | 0.217832 | 0.863129 | 86.426% |
| 1 | 0 | 172894.5 | 17.724% | 4.129135 | 54.540% | 0.108352 | 1.876959 | 0.358689 | 0.831107 | 81.289% |
| 2 | 0 | 188778.9 | 28.540% | 3.440903 | 62.117% | 0.082583 | 1.416528 | 0.300861 | 0.813350 | 78.442% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
