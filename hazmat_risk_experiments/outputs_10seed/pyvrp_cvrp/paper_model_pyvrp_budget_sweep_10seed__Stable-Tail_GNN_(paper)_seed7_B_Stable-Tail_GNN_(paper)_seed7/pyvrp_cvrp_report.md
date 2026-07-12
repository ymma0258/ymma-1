# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.6 | 0.000% | 9.631780 | 0.000% | 0.282781 | 3.092624 | 0.209249 | 0.875171 | 90.287% |
| 0.25 | 0 | 158027.0 | 7.260% | 7.919977 | 17.772% | 0.228291 | 2.636049 | 0.221133 | 0.874460 | 89.217% |
| 0.5 | 0 | 167422.8 | 13.637% | 5.900149 | 38.743% | 0.166302 | 2.139184 | 0.278127 | 0.857694 | 85.927% |
| 1 | 0 | 178910.2 | 21.435% | 3.948664 | 59.004% | 0.100465 | 1.360031 | 0.250575 | 0.824804 | 79.979% |
| 2 | 0 | 195681.3 | 32.818% | 3.410579 | 64.590% | 0.079892 | 1.101759 | 0.227252 | 0.811728 | 77.459% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
