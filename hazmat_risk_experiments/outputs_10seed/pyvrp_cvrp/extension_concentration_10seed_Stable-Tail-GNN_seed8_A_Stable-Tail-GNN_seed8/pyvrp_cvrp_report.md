# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.634359 | 0.000% | 0.229405 | 2.385096 | 0.166464 | 0.885783 | 90.393% |
| 1 | 0 | 157997.4 | 17.911% | 3.011525 | 60.553% | 0.074084 | 0.869025 | 0.199251 | 0.822900 | 80.016% |
| 1 | 0.5 | 164566.8 | 22.813% | 2.699937 | 64.634% | 0.059143 | 0.963230 | 0.276212 | 0.810422 | 77.764% |
| 1 | 1 | 168972.5 | 26.101% | 2.309236 | 69.752% | 0.044565 | 0.853275 | 0.310009 | 0.793104 | 74.510% |
| 1 | 2 | 177460.3 | 32.436% | 2.061423 | 72.998% | 0.041343 | 0.858176 | 0.305911 | 0.766279 | 70.630% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
