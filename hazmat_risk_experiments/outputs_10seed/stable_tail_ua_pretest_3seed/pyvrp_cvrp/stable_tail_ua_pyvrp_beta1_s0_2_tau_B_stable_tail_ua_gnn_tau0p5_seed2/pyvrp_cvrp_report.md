# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 16.051966 | 0.000% | 0.181664 | 4.890753 | 0.188279 | 0.845959 | 89.477% |
| 1 | 0 | 184693.3 | 26.311% | 8.544858 | 46.768% | 0.107776 | 3.397828 | 0.303807 | 0.807046 | 82.158% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
