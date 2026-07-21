# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.2 | 0.000% | 6.989701 | 0.000% | 0.190092 | 2.384484 | 0.254233 | 0.868000 | 88.812% |
| 0.25 | 0 | 155563.8 | 5.589% | 5.864269 | 16.101% | 0.143971 | 2.184706 | 0.279044 | 0.863565 | 87.895% |
| 0.5 | 0 | 163606.7 | 11.048% | 4.529014 | 35.204% | 0.117049 | 1.697270 | 0.254106 | 0.851148 | 85.300% |
| 1 | 0 | 175408.1 | 19.058% | 3.645720 | 47.842% | 0.095570 | 1.400612 | 0.290118 | 0.837705 | 82.513% |
| 2 | 0 | 193198.5 | 31.133% | 2.752012 | 60.628% | 0.067599 | 1.125326 | 0.298952 | 0.808760 | 77.453% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
