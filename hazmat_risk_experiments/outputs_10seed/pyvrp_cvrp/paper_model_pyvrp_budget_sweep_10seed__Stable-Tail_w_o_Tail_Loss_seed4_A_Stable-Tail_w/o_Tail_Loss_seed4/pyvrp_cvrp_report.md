# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134065.0 | 0.000% | 7.211890 | 0.000% | 0.239806 | 2.149820 | 0.190974 | 0.869612 | 89.551% |
| 0.25 | 0 | 142751.3 | 6.479% | 5.294828 | 26.582% | 0.146086 | 1.707811 | 0.204258 | 0.860454 | 88.464% |
| 0.5 | 0 | 149376.0 | 11.421% | 4.207521 | 41.659% | 0.106308 | 1.460544 | 0.229587 | 0.847867 | 86.076% |
| 1 | 0 | 159303.8 | 18.826% | 2.976265 | 58.731% | 0.073060 | 0.953227 | 0.248661 | 0.803757 | 79.990% |
| 2 | 0 | 174271.9 | 29.991% | 2.625753 | 63.591% | 0.063426 | 0.793356 | 0.236177 | 0.795724 | 78.036% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
