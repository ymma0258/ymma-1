# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.860219 | 0.000% | 0.229249 | 2.176818 | 0.146225 | 0.866491 | 88.716% |
| 0.25 | 0 | 143365.7 | 6.938% | 5.135502 | 34.665% | 0.150947 | 1.527345 | 0.217497 | 0.845506 | 85.318% |
| 0.5 | 0 | 149378.8 | 11.423% | 3.897795 | 50.411% | 0.113402 | 1.310425 | 0.245734 | 0.816814 | 81.322% |
| 1 | 0 | 158729.0 | 18.397% | 2.863186 | 63.574% | 0.075921 | 0.912618 | 0.257517 | 0.773289 | 75.131% |
| 2 | 0 | 173258.7 | 29.235% | 2.296371 | 70.785% | 0.054137 | 0.887476 | 0.295738 | 0.733516 | 69.611% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
