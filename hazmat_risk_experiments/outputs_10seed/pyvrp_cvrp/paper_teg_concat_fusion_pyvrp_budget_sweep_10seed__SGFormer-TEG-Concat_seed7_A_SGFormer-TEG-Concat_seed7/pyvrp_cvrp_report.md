# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.9 | 0.000% | 8.556159 | 0.000% | 0.277046 | 2.756146 | 0.227136 | 0.875430 | 88.187% |
| 0.25 | 0 | 143289.2 | 6.880% | 5.264002 | 38.477% | 0.150548 | 1.967662 | 0.291204 | 0.851123 | 82.744% |
| 0.5 | 0 | 149310.2 | 11.372% | 4.506595 | 47.329% | 0.125967 | 1.750548 | 0.293025 | 0.834926 | 80.334% |
| 1 | 0 | 156839.6 | 16.988% | 2.020711 | 76.383% | 0.033050 | 0.567346 | 0.182555 | 0.694176 | 58.813% |
| 2 | 0 | 167214.0 | 24.726% | 1.997021 | 76.660% | 0.031049 | 0.538844 | 0.177304 | 0.690144 | 58.169% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
