# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.599006 | 0.000% | 0.253180 | 2.463378 | 0.141025 | 0.849978 | 88.337% |
| 1 | 0 | 160359.7 | 19.674% | 3.631858 | 57.764% | 0.098279 | 1.215457 | 0.235584 | 0.765055 | 76.307% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
