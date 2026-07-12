# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 8.960568 | 0.000% | 0.293825 | 2.569857 | 0.179441 | 0.871531 | 89.304% |
| 0.25 | 0 | 143422.1 | 6.714% | 5.971740 | 33.355% | 0.169408 | 2.088780 | 0.252791 | 0.857988 | 86.707% |
| 0.5 | 0 | 149561.2 | 11.282% | 4.593247 | 48.739% | 0.130755 | 1.698326 | 0.260137 | 0.835405 | 83.155% |
| 1 | 0 | 159005.5 | 18.309% | 3.424944 | 61.778% | 0.093710 | 1.134838 | 0.219458 | 0.801199 | 77.930% |
| 2 | 0 | 172047.8 | 28.014% | 2.629469 | 70.655% | 0.062944 | 0.845452 | 0.239451 | 0.761842 | 71.725% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
