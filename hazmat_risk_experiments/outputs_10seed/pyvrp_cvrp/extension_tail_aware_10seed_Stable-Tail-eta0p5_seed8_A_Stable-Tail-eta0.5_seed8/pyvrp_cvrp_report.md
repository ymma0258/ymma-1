# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 9.711498 | 0.000% | 0.195760 | 2.955939 | 0.157834 | 0.885359 | 90.263% |
| 1 | 0 | 159550.5 | 19.070% | 4.020162 | 58.604% | 0.062615 | 1.330022 | 0.258820 | 0.830108 | 80.433% |
| 2 | 0 | 174252.6 | 30.042% | 2.941822 | 69.708% | 0.043632 | 1.211926 | 0.346312 | 0.794969 | 74.428% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
