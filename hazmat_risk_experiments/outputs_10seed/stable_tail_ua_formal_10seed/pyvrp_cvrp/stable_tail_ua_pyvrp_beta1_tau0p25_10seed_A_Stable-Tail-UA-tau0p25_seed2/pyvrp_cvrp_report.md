# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 11.833187 | 0.000% | 0.267835 | 3.214132 | 0.131295 | 0.856477 | 89.010% |
| 1 | 0 | 161100.3 | 20.226% | 5.082990 | 57.045% | 0.095221 | 1.766778 | 0.271633 | 0.792160 | 78.879% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
