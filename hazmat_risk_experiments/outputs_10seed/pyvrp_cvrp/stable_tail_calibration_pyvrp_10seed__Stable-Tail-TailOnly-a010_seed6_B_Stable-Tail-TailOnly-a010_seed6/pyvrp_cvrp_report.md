# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.9 | 0.000% | 9.036942 | 0.000% | 0.272969 | 3.125155 | 0.237074 | 0.870667 | 89.303% |
| 0.25 | 0 | 158253.4 | 7.609% | 7.981403 | 11.680% | 0.215058 | 2.592052 | 0.215302 | 0.869300 | 89.180% |
| 0.5 | 0 | 168582.7 | 14.632% | 6.032480 | 33.246% | 0.149841 | 2.085558 | 0.250035 | 0.853992 | 86.241% |
| 1 | 0 | 182012.2 | 23.764% | 4.200149 | 53.522% | 0.104143 | 1.625361 | 0.326474 | 0.826286 | 81.051% |
| 2 | 0 | 201978.0 | 37.340% | 3.766551 | 58.321% | 0.094524 | 1.459641 | 0.354298 | 0.817458 | 79.310% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
