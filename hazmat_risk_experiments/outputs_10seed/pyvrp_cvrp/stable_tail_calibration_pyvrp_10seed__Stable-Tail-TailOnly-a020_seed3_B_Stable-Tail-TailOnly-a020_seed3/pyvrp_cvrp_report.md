# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.4 | 0.000% | 7.201748 | 0.000% | 0.214282 | 2.448944 | 0.253553 | 0.872341 | 89.291% |
| 0.25 | 0 | 155019.8 | 5.362% | 5.875069 | 18.422% | 0.146119 | 2.169409 | 0.289441 | 0.866965 | 88.162% |
| 0.5 | 0 | 162821.9 | 10.665% | 4.879580 | 32.245% | 0.123167 | 2.075969 | 0.294866 | 0.856201 | 86.160% |
| 1 | 0 | 174350.8 | 18.501% | 3.527860 | 51.014% | 0.090380 | 1.464901 | 0.318455 | 0.838004 | 82.270% |
| 2 | 0 | 190525.6 | 29.494% | 2.781490 | 61.378% | 0.069971 | 1.166598 | 0.306811 | 0.810625 | 77.705% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
