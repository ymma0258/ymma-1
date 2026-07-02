# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 8.836971 | 0.000% | 0.271881 | 3.115800 | 0.256232 | 0.877868 | 90.345% |
| 1 | 0 | 175014.0 | 19.692% | 4.017026 | 54.543% | 0.089802 | 1.390717 | 0.224106 | 0.823717 | 80.669% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
