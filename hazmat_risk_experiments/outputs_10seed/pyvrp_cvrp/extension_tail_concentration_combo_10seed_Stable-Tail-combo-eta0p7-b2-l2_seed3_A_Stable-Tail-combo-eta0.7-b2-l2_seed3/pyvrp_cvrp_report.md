# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 6.695492 | 0.000% | 0.195570 | 2.189409 | 0.216915 | 0.875815 | 89.250% |
| 2 | 2 | 178212.1 | 32.996% | 1.475794 | 77.958% | 0.023173 | 0.468998 | 0.234420 | 0.666867 | 59.010% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
