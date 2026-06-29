# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.3 | 0.000% | 7.445017 | 0.000% | 0.235965 | 2.137336 | 0.143465 | 0.862420 | 88.653% |
| 1 | 0 | 157056.3 | 17.209% | 3.024730 | 59.372% | 0.083311 | 1.009277 | 0.219417 | 0.788156 | 77.447% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
