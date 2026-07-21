# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.5 | 0.000% | 8.628892 | 0.000% | 0.263847 | 2.895398 | 0.228417 | 0.882557 | 90.132% |
| 0.25 | 0 | 156182.3 | 6.152% | 7.623576 | 11.651% | 0.207843 | 2.287414 | 0.195345 | 0.882737 | 89.927% |
| 0.5 | 0 | 164618.3 | 11.886% | 5.801967 | 32.761% | 0.142821 | 1.971797 | 0.278859 | 0.867975 | 87.197% |
| 1 | 0 | 174797.0 | 18.804% | 3.944387 | 54.289% | 0.097977 | 1.443180 | 0.302843 | 0.833647 | 81.708% |
| 2 | 0 | 189441.3 | 28.757% | 3.039276 | 64.778% | 0.076178 | 1.009737 | 0.300490 | 0.808959 | 77.340% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
