# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 7.683610 | 0.000% | 0.230730 | 2.674220 | 0.242297 | 0.855846 | 88.816% |
| 1 | 0 | 179169.6 | 22.274% | 3.982434 | 48.170% | 0.100015 | 1.304265 | 0.272218 | 0.809840 | 80.996% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
