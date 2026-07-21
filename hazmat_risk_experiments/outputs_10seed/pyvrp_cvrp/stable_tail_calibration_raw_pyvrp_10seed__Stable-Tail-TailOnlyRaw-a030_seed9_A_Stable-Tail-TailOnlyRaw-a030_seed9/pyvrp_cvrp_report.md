# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.7 | 0.000% | 9.785925 | 0.000% | 0.326767 | 2.882331 | 0.176583 | 0.875103 | 90.134% |
| 0.25 | 0 | 143463.5 | 6.851% | 6.122600 | 37.435% | 0.171264 | 2.088452 | 0.253062 | 0.864141 | 88.124% |
| 0.5 | 0 | 149850.2 | 11.608% | 4.708004 | 51.890% | 0.130850 | 1.749210 | 0.265406 | 0.838217 | 84.754% |
| 1 | 0 | 158979.3 | 18.407% | 3.202870 | 67.271% | 0.075774 | 1.266045 | 0.314274 | 0.793528 | 78.005% |
| 2 | 0 | 172436.5 | 28.430% | 2.525981 | 74.188% | 0.052874 | 0.775325 | 0.237908 | 0.753314 | 72.438% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
