# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.8 | 0.000% | 9.954021 | 0.000% | 0.316510 | 3.415555 | 0.267192 | 0.873462 | 90.184% |
| 0.25 | 0 | 156249.2 | 6.053% | 8.255301 | 17.066% | 0.241346 | 2.747395 | 0.253020 | 0.869452 | 88.859% |
| 0.5 | 0 | 164494.8 | 11.650% | 6.739304 | 32.296% | 0.174524 | 2.071304 | 0.222626 | 0.862257 | 86.890% |
| 1 | 0 | 174521.0 | 18.455% | 3.969140 | 60.125% | 0.087868 | 1.398003 | 0.253053 | 0.819108 | 79.631% |
| 2 | 0 | 188475.1 | 27.926% | 3.354212 | 66.303% | 0.068654 | 1.159017 | 0.243907 | 0.797005 | 76.082% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
