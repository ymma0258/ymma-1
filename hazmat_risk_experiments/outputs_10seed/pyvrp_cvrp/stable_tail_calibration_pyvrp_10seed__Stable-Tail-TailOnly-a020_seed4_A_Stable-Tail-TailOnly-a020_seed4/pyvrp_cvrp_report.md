# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 9.336112 | 0.000% | 0.288654 | 2.625013 | 0.154331 | 0.882315 | 90.709% |
| 0.25 | 0 | 142788.2 | 6.560% | 6.874495 | 26.367% | 0.220746 | 2.133998 | 0.220146 | 0.875620 | 89.163% |
| 0.5 | 0 | 149566.5 | 11.618% | 5.225364 | 44.031% | 0.156882 | 1.729206 | 0.255708 | 0.860439 | 86.437% |
| 1 | 0 | 158800.7 | 18.510% | 3.712227 | 60.238% | 0.099893 | 1.361933 | 0.323327 | 0.825052 | 81.191% |
| 2 | 0 | 173568.2 | 29.530% | 2.963755 | 68.255% | 0.071546 | 1.156541 | 0.366545 | 0.799664 | 77.050% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
