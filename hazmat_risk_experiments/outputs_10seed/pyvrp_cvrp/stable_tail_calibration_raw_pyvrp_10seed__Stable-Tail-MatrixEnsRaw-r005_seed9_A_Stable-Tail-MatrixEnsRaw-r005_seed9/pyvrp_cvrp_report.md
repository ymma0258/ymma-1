# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.017928 | 0.000% | 0.254656 | 2.280966 | 0.159528 | 0.870045 | 89.391% |
| 0.25 | 0 | 143312.7 | 6.951% | 5.565758 | 30.584% | 0.159959 | 1.735468 | 0.217085 | 0.858410 | 87.472% |
| 0.5 | 0 | 149685.8 | 11.707% | 4.200596 | 47.610% | 0.101228 | 1.540415 | 0.255941 | 0.836884 | 84.247% |
| 1 | 0 | 158674.5 | 18.416% | 2.700292 | 66.322% | 0.063082 | 0.973829 | 0.271146 | 0.772658 | 75.545% |
| 2 | 0 | 172660.6 | 28.853% | 2.253261 | 71.897% | 0.050199 | 0.690825 | 0.223344 | 0.740212 | 70.806% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
