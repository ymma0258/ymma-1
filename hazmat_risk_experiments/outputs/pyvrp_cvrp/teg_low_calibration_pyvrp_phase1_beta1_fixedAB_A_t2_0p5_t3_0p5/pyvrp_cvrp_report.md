# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.141519 | 0.000% | 0.271561 | 2.688025 | 0.231690 | 0.843476 | 87.033% |
| 1 | 0 | 158739.6 | 18.465% | 3.276100 | 59.761% | 0.081415 | 1.098740 | 0.252541 | 0.720672 | 71.117% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
