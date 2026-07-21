# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.6 | 0.000% | 7.716044 | 0.000% | 0.211839 | 2.589709 | 0.258143 | 0.878701 | 89.692% |
| 0.25 | 0 | 156555.3 | 6.310% | 6.367769 | 17.474% | 0.156077 | 2.230214 | 0.263615 | 0.871833 | 88.450% |
| 0.5 | 0 | 165286.2 | 12.238% | 4.508044 | 41.576% | 0.114608 | 1.656996 | 0.252937 | 0.846955 | 83.927% |
| 1 | 0 | 175732.8 | 19.332% | 3.056055 | 60.394% | 0.074803 | 1.118325 | 0.286271 | 0.807260 | 77.773% |
| 2 | 0 | 190414.9 | 29.302% | 2.528203 | 67.234% | 0.056129 | 0.937910 | 0.278461 | 0.784180 | 73.529% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
