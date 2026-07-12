# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 8.584720 | 0.000% | 0.265712 | 2.553271 | 0.176626 | 0.836795 | 86.208% |
| 0.25 | 0 | 143981.3 | 7.343% | 7.078352 | 17.547% | 0.189669 | 2.096011 | 0.170019 | 0.828779 | 85.589% |
| 0.5 | 0 | 150666.8 | 12.328% | 4.929244 | 42.581% | 0.135679 | 1.975126 | 0.283899 | 0.784871 | 79.547% |
| 1 | 0 | 161162.5 | 20.153% | 3.506901 | 59.149% | 0.086663 | 1.422605 | 0.308151 | 0.720053 | 71.180% |
| 2 | 0 | 177313.0 | 32.193% | 2.946379 | 65.679% | 0.059501 | 1.038705 | 0.274825 | 0.673964 | 65.477% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
