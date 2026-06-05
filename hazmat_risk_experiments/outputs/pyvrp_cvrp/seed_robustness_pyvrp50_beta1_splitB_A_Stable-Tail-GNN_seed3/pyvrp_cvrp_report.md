# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 6.421212 | 0.000% | 0.190014 | 2.233108 | 0.243878 | 0.872838 | 88.920% |
| 1 | 0 | 154698.8 | 15.449% | 2.449774 | 61.849% | 0.057540 | 0.773952 | 0.208916 | 0.775251 | 74.943% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
