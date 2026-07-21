# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.066185 | 0.000% | 0.193458 | 2.357123 | 0.246090 | 0.877175 | 89.380% |
| 0.25 | 0 | 156581.5 | 6.568% | 6.079861 | 13.958% | 0.149629 | 1.933077 | 0.234037 | 0.873480 | 88.555% |
| 0.5 | 0 | 164837.3 | 12.187% | 4.425569 | 37.370% | 0.113001 | 1.511947 | 0.208896 | 0.851592 | 84.703% |
| 1 | 0 | 175312.7 | 19.317% | 2.993088 | 57.642% | 0.076849 | 1.140459 | 0.281400 | 0.812350 | 78.506% |
| 2 | 0 | 190723.7 | 29.805% | 2.309507 | 67.316% | 0.047298 | 0.834074 | 0.279956 | 0.777809 | 72.561% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
