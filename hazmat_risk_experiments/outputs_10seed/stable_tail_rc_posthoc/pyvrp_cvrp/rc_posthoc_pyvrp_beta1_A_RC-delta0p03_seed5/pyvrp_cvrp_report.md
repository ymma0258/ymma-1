# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.9 | 0.000% | 6.708935 | 0.000% | 0.202210 | 1.957876 | 0.172157 | 0.874651 | 89.232% |
| 1 | 0 | 155586.7 | 16.053% | 2.338977 | 65.136% | 0.060071 | 0.889887 | 0.306952 | 0.776024 | 74.272% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
