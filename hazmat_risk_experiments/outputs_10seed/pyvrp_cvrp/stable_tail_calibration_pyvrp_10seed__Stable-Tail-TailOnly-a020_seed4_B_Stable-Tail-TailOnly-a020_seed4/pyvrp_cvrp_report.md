# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147196.9 | 0.000% | 8.847538 | 0.000% | 0.272234 | 2.826545 | 0.203802 | 0.876664 | 89.561% |
| 0.25 | 0 | 155426.1 | 5.591% | 7.575373 | 14.379% | 0.206364 | 2.371909 | 0.222462 | 0.874304 | 88.669% |
| 0.5 | 0 | 163439.8 | 11.035% | 6.264190 | 29.198% | 0.176145 | 2.056370 | 0.230715 | 0.869335 | 87.045% |
| 1 | 0 | 173620.1 | 17.951% | 4.005474 | 54.728% | 0.103314 | 1.577067 | 0.304181 | 0.824245 | 80.543% |
| 2 | 0 | 189195.3 | 28.532% | 3.298950 | 62.713% | 0.069907 | 1.286939 | 0.307286 | 0.806393 | 77.549% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
