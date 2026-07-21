# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.122579 | 0.000% | 0.214229 | 2.340882 | 0.218508 | 0.869294 | 89.157% |
| 0.25 | 0 | 157713.3 | 7.339% | 6.273315 | 11.924% | 0.158070 | 2.133599 | 0.243314 | 0.867741 | 89.178% |
| 0.5 | 0 | 168006.7 | 14.344% | 4.558618 | 35.998% | 0.116379 | 1.632341 | 0.274386 | 0.852878 | 85.830% |
| 1 | 0 | 181213.4 | 23.333% | 3.471333 | 51.263% | 0.085765 | 1.350084 | 0.319126 | 0.827781 | 81.543% |
| 2 | 0 | 202335.9 | 37.708% | 2.946447 | 58.632% | 0.074800 | 1.126598 | 0.351981 | 0.815759 | 79.068% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
