# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.279310 | 0.000% | 0.255644 | 2.430843 | 0.152828 | 0.858015 | 88.982% |
| 1 | 0 | 161451.5 | 20.488% | 3.497744 | 57.753% | 0.080167 | 1.131657 | 0.271005 | 0.784408 | 77.932% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
