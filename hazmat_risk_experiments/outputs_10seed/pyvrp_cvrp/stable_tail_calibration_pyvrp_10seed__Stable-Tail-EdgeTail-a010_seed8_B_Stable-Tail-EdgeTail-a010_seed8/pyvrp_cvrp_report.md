# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 7.440608 | 0.000% | 0.216320 | 2.318888 | 0.200778 | 0.859319 | 87.573% |
| 0.25 | 0 | 156802.7 | 6.477% | 6.256835 | 15.910% | 0.149776 | 1.985684 | 0.190565 | 0.854875 | 86.790% |
| 0.5 | 0 | 165331.2 | 12.269% | 5.106990 | 31.363% | 0.123562 | 1.575944 | 0.204093 | 0.843926 | 84.426% |
| 1 | 0 | 176415.0 | 19.795% | 3.145974 | 57.719% | 0.073182 | 1.151084 | 0.278209 | 0.788928 | 76.284% |
| 2 | 0 | 191627.5 | 30.125% | 2.460329 | 66.934% | 0.053378 | 0.760419 | 0.223357 | 0.751059 | 70.517% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
