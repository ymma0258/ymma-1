# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.4 | 0.000% | 7.217449 | 0.000% | 0.228127 | 2.147252 | 0.175513 | 0.869870 | 88.573% |
| 0.25 | 0 | 141944.7 | 5.563% | 5.096644 | 29.384% | 0.147564 | 1.482736 | 0.173136 | 0.856106 | 86.900% |
| 0.5 | 0 | 147293.3 | 9.541% | 3.624762 | 49.778% | 0.107359 | 1.163084 | 0.232452 | 0.833505 | 83.019% |
| 1 | 0 | 155298.5 | 15.494% | 2.383906 | 66.970% | 0.062401 | 0.695248 | 0.203846 | 0.768155 | 74.029% |
| 2 | 0 | 167671.0 | 24.695% | 2.133963 | 70.433% | 0.052458 | 0.679485 | 0.253756 | 0.750762 | 71.120% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
