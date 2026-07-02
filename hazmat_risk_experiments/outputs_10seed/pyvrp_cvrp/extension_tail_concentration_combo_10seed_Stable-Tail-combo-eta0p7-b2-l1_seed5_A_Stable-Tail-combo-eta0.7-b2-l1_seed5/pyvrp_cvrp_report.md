# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.152817 | 0.000% | 0.175570 | 1.791873 | 0.170530 | 0.873796 | 89.035% |
| 2 | 1 | 175859.5 | 31.241% | 1.476559 | 76.002% | 0.029861 | 0.419955 | 0.206323 | 0.689259 | 60.723% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
