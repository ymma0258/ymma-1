# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.3 | 0.000% | 9.677181 | 0.000% | 0.311751 | 2.715323 | 0.161152 | 0.876641 | 90.013% |
| 1 | 0 | 158549.7 | 18.205% | 3.265152 | 66.259% | 0.071692 | 1.141259 | 0.271003 | 0.806493 | 77.657% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
