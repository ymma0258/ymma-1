# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.1 | 0.000% | 8.075892 | 0.000% | 0.240977 | 2.457038 | 0.208601 | 0.827743 | 85.256% |
| 0.25 | 0 | 156368.2 | 6.135% | 6.735703 | 16.595% | 0.201088 | 1.953382 | 0.181137 | 0.816449 | 83.918% |
| 0.5 | 0 | 164880.9 | 11.913% | 5.175383 | 35.916% | 0.128306 | 1.584965 | 0.200126 | 0.776792 | 78.897% |
| 1 | 0 | 175025.5 | 18.798% | 3.458609 | 57.174% | 0.065272 | 1.129308 | 0.230029 | 0.694805 | 69.063% |
| 2 | 0 | 190407.6 | 29.239% | 2.859688 | 64.590% | 0.050244 | 0.938112 | 0.198258 | 0.647127 | 63.055% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
