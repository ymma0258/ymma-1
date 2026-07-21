# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.3 | 0.000% | 8.590351 | 0.000% | 0.239407 | 2.835881 | 0.248553 | 0.886477 | 90.812% |
| 0.25 | 0 | 156647.1 | 6.516% | 7.087153 | 17.499% | 0.174725 | 2.520212 | 0.252733 | 0.880674 | 89.450% |
| 0.5 | 0 | 165202.0 | 12.333% | 5.055864 | 41.145% | 0.130822 | 1.773844 | 0.246642 | 0.858543 | 85.712% |
| 1 | 0 | 175101.6 | 19.065% | 3.316876 | 61.388% | 0.085808 | 1.318030 | 0.293475 | 0.821375 | 79.515% |
| 2 | 0 | 189659.4 | 28.964% | 2.630916 | 69.374% | 0.055057 | 1.025884 | 0.314514 | 0.793520 | 74.543% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
