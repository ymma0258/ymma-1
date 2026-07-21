# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 9.541116 | 0.000% | 0.295624 | 2.699752 | 0.156615 | 0.883797 | 90.908% |
| 0.25 | 0 | 142515.4 | 6.356% | 7.139858 | 25.167% | 0.225732 | 2.183491 | 0.203168 | 0.877522 | 89.472% |
| 0.5 | 0 | 149240.6 | 11.375% | 5.285278 | 44.605% | 0.163583 | 1.655323 | 0.236387 | 0.858945 | 86.269% |
| 1 | 0 | 158341.2 | 18.167% | 3.784297 | 60.337% | 0.102078 | 1.421635 | 0.334237 | 0.827203 | 81.397% |
| 2 | 0 | 173255.0 | 29.297% | 3.106561 | 67.440% | 0.076775 | 1.229641 | 0.369772 | 0.806438 | 78.020% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
