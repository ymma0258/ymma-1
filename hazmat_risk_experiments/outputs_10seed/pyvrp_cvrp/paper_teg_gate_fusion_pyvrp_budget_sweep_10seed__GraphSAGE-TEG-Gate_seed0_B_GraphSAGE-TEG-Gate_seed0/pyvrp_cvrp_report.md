# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.2 | 0.000% | 7.869701 | 0.000% | 0.230274 | 2.490451 | 0.215916 | 0.875140 | 89.213% |
| 0.25 | 0 | 157192.4 | 6.936% | 6.881425 | 12.558% | 0.191160 | 2.135907 | 0.210989 | 0.872554 | 88.639% |
| 0.5 | 0 | 166477.9 | 13.252% | 5.068392 | 35.596% | 0.141036 | 1.565575 | 0.212045 | 0.852989 | 85.294% |
| 1 | 0 | 177463.0 | 20.725% | 3.341328 | 57.542% | 0.073092 | 1.288710 | 0.305996 | 0.819402 | 79.309% |
| 2 | 0 | 194504.0 | 32.318% | 2.686421 | 65.864% | 0.058280 | 1.060197 | 0.319950 | 0.797741 | 74.930% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
