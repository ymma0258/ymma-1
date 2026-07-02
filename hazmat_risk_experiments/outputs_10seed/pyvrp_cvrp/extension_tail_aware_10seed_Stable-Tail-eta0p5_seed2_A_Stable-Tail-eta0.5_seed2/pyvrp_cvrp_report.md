# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 11.192205 | 0.000% | 0.232981 | 3.240078 | 0.154013 | 0.872891 | 89.894% |
| 1 | 0 | 158206.9 | 18.067% | 4.523831 | 59.581% | 0.074295 | 1.382250 | 0.242066 | 0.824934 | 79.981% |
| 2 | 0 | 172654.4 | 28.849% | 3.980239 | 64.437% | 0.062167 | 1.445166 | 0.325308 | 0.806779 | 76.931% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
