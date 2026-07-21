# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 6.854156 | 0.000% | 0.211335 | 2.128452 | 0.190756 | 0.860198 | 87.757% |
| 0.25 | 0 | 156272.6 | 6.358% | 5.603895 | 18.241% | 0.130190 | 1.873970 | 0.216272 | 0.854279 | 86.793% |
| 0.5 | 0 | 164666.9 | 12.071% | 4.521979 | 34.026% | 0.108956 | 1.403756 | 0.205719 | 0.840527 | 84.112% |
| 1 | 0 | 175572.2 | 19.493% | 2.693459 | 60.703% | 0.064081 | 0.821513 | 0.189548 | 0.781567 | 75.306% |
| 2 | 0 | 190315.9 | 29.528% | 2.188654 | 68.068% | 0.045642 | 0.616717 | 0.183113 | 0.750743 | 70.395% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
