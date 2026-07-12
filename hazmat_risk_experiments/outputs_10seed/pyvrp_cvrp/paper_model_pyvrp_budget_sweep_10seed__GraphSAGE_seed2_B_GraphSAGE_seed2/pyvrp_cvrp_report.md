# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.2 | 0.000% | 9.151099 | 0.000% | 0.284828 | 3.532545 | 0.317795 | 0.874227 | 89.022% |
| 0.25 | 0 | 157722.8 | 7.054% | 7.886668 | 13.817% | 0.238517 | 2.933033 | 0.291775 | 0.872819 | 88.919% |
| 0.5 | 0 | 167018.0 | 13.363% | 6.317162 | 30.968% | 0.166305 | 2.497795 | 0.300723 | 0.867172 | 87.146% |
| 1 | 0 | 180901.9 | 22.787% | 4.544600 | 50.338% | 0.115701 | 1.708685 | 0.297700 | 0.845099 | 82.925% |
| 2 | 0 | 201211.8 | 36.572% | 3.824435 | 58.208% | 0.087982 | 1.761251 | 0.363648 | 0.828512 | 79.796% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
