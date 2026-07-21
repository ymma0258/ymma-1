# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.944611 | 0.000% | 0.314860 | 3.482760 | 0.258381 | 0.874401 | 90.081% |
| 0.25 | 0 | 155599.0 | 5.852% | 7.598257 | 23.594% | 0.198126 | 2.490480 | 0.248442 | 0.868085 | 88.306% |
| 0.5 | 0 | 163919.9 | 11.512% | 6.774622 | 31.876% | 0.181506 | 2.108221 | 0.228140 | 0.862672 | 87.201% |
| 1 | 0 | 173616.7 | 18.109% | 4.076852 | 59.004% | 0.094257 | 1.332931 | 0.234655 | 0.817938 | 79.856% |
| 2 | 0 | 187317.5 | 27.429% | 3.447386 | 65.334% | 0.069621 | 1.152887 | 0.268776 | 0.802857 | 76.935% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
