# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 7.344839 | 0.000% | 0.202040 | 2.397013 | 0.235627 | 0.876325 | 89.282% |
| 0.25 | 0 | 157278.4 | 6.897% | 6.070990 | 17.343% | 0.147984 | 2.251746 | 0.275488 | 0.869008 | 87.835% |
| 0.5 | 0 | 165453.2 | 12.453% | 4.409433 | 39.966% | 0.111533 | 1.506254 | 0.229065 | 0.847312 | 83.937% |
| 1 | 0 | 175980.0 | 19.608% | 3.025526 | 58.807% | 0.075107 | 1.057554 | 0.258309 | 0.806142 | 77.587% |
| 2 | 0 | 191313.3 | 30.030% | 2.411764 | 67.164% | 0.049776 | 0.920034 | 0.290095 | 0.778151 | 72.530% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
