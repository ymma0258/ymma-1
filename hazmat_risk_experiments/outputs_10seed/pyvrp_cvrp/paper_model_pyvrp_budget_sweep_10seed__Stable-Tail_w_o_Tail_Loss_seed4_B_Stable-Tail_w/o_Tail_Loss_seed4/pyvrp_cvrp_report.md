# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.2 | 0.000% | 7.358761 | 0.000% | 0.229450 | 2.243131 | 0.185037 | 0.855923 | 88.685% |
| 0.25 | 0 | 157979.0 | 7.276% | 5.658266 | 23.108% | 0.163237 | 1.724153 | 0.194795 | 0.851958 | 88.022% |
| 0.5 | 0 | 168176.1 | 14.200% | 4.631629 | 37.060% | 0.118438 | 1.426778 | 0.212715 | 0.843935 | 86.015% |
| 1 | 0 | 180387.2 | 22.492% | 3.483322 | 52.664% | 0.089479 | 1.252791 | 0.295665 | 0.817554 | 81.873% |
| 2 | 0 | 201103.9 | 36.560% | 2.845084 | 61.337% | 0.057785 | 1.070550 | 0.314327 | 0.797436 | 78.098% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
