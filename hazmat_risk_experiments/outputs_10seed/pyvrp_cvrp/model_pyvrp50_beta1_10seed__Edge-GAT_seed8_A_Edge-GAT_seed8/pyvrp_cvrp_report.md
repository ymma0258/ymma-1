# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.807568 | 0.000% | 0.242873 | 2.309584 | 0.156542 | 0.871568 | 89.672% |
| 1 | 0 | 160238.4 | 19.583% | 3.270998 | 58.105% | 0.080843 | 1.140913 | 0.300417 | 0.805205 | 78.945% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
