# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 9.230143 | 0.000% | 0.278618 | 3.067671 | 0.228676 | 0.872341 | 89.536% |
| 0.25 | 0 | 157789.7 | 7.391% | 8.116557 | 12.065% | 0.204162 | 2.665663 | 0.232315 | 0.870659 | 89.534% |
| 0.5 | 0 | 168103.4 | 14.410% | 6.076992 | 34.161% | 0.157480 | 2.147660 | 0.257890 | 0.858106 | 86.630% |
| 1 | 0 | 180786.9 | 23.042% | 4.097711 | 55.605% | 0.103710 | 1.475336 | 0.317851 | 0.826565 | 80.867% |
| 2 | 0 | 201128.2 | 36.887% | 3.711647 | 59.788% | 0.094127 | 1.432644 | 0.344547 | 0.817357 | 79.218% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
