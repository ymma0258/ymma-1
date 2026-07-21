# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 7.806516 | 0.000% | 0.237273 | 2.589904 | 0.233709 | 0.874261 | 89.067% |
| 0.25 | 0 | 156573.9 | 6.322% | 6.710025 | 14.046% | 0.171450 | 2.204781 | 0.227841 | 0.869812 | 88.382% |
| 0.5 | 0 | 165512.3 | 12.392% | 5.400869 | 30.816% | 0.126891 | 1.910199 | 0.277201 | 0.857852 | 85.918% |
| 1 | 0 | 175750.3 | 19.344% | 3.469350 | 55.558% | 0.086318 | 1.220911 | 0.282221 | 0.815219 | 79.279% |
| 2 | 0 | 191477.5 | 30.023% | 2.753121 | 64.733% | 0.065733 | 0.865658 | 0.265737 | 0.788558 | 74.587% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
