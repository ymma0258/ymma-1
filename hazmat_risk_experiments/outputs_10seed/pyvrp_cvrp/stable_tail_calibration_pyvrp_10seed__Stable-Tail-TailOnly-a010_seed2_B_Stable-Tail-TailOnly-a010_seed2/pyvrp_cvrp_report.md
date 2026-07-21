# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.7 | 0.000% | 9.220984 | 0.000% | 0.285666 | 3.404918 | 0.312097 | 0.878466 | 90.015% |
| 0.25 | 0 | 156468.0 | 6.346% | 8.047594 | 12.725% | 0.242312 | 3.367635 | 0.339882 | 0.876124 | 89.594% |
| 0.5 | 0 | 165169.4 | 12.260% | 6.595837 | 28.469% | 0.197747 | 2.639241 | 0.317308 | 0.867077 | 87.546% |
| 1 | 0 | 177580.6 | 20.696% | 4.821038 | 47.717% | 0.126439 | 1.842646 | 0.252404 | 0.848774 | 84.117% |
| 2 | 0 | 196028.8 | 33.234% | 3.784502 | 58.958% | 0.093392 | 1.788857 | 0.398564 | 0.831797 | 80.721% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
