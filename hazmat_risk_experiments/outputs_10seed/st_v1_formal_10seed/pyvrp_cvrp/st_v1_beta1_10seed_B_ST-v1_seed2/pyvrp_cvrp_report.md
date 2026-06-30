# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 9.996386 | 0.000% | 0.308855 | 3.494307 | 0.252170 | 0.876783 | 90.774% |
| 1 | 0 | 178586.5 | 21.600% | 4.454388 | 55.440% | 0.118921 | 1.662848 | 0.312569 | 0.849164 | 83.254% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
