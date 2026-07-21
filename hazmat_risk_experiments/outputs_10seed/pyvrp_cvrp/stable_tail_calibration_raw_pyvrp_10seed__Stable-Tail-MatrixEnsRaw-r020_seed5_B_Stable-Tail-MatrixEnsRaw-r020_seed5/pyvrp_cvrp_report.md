# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.9 | 0.000% | 6.225508 | 0.000% | 0.193985 | 2.013688 | 0.214261 | 0.875033 | 89.082% |
| 0.25 | 0 | 156576.4 | 6.468% | 5.457848 | 12.331% | 0.137994 | 1.766238 | 0.228610 | 0.873985 | 88.796% |
| 0.5 | 0 | 164769.7 | 12.040% | 3.816754 | 38.692% | 0.091579 | 1.232814 | 0.233978 | 0.845683 | 84.223% |
| 1 | 0 | 175827.1 | 19.558% | 2.691500 | 56.767% | 0.067016 | 0.956844 | 0.301661 | 0.814616 | 78.934% |
| 2 | 0 | 191283.7 | 30.068% | 2.230280 | 64.175% | 0.053288 | 0.714232 | 0.266142 | 0.793553 | 75.287% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
