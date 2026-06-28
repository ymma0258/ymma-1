# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 12.534722 | 0.000% | 0.279169 | 4.090174 | 0.219148 | 0.882240 | 90.248% |
| 1 | 0 | 181450.3 | 23.662% | 5.428920 | 56.689% | 0.064583 | 2.330837 | 0.383686 | 0.840729 | 80.733% |
| 2 | 0 | 202980.7 | 38.335% | 4.976317 | 60.300% | 0.058264 | 1.994114 | 0.365785 | 0.831199 | 79.097% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
