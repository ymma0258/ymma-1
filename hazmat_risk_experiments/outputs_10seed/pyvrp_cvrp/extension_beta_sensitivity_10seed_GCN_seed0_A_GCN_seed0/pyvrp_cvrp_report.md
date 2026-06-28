# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.181534 | 0.000% | 0.205961 | 2.330343 | 0.206503 | 0.863271 | 88.639% |
| 0.5 | 0 | 148581.9 | 10.884% | 4.060203 | 43.463% | 0.121491 | 1.543766 | 0.272230 | 0.829475 | 83.729% |
| 1 | 0 | 157100.0 | 17.241% | 2.601871 | 63.770% | 0.056984 | 0.833768 | 0.194819 | 0.763200 | 74.705% |
| 1.5 | 0 | 163677.3 | 22.149% | 2.411297 | 66.424% | 0.052967 | 0.795704 | 0.254162 | 0.748498 | 72.647% |
| 2 | 0 | 169866.0 | 26.768% | 2.298080 | 68.000% | 0.047516 | 0.696864 | 0.227409 | 0.738236 | 71.128% |
| 3 | 0 | 179837.9 | 34.210% | 1.766117 | 75.408% | 0.030220 | 0.578294 | 0.252346 | 0.677128 | 62.642% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
