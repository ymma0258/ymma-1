# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 10.294561 | 0.000% | 0.308151 | 3.109896 | 0.190835 | 0.878990 | 90.693% |
| 0.25 | 0 | 157854.6 | 7.192% | 8.418959 | 18.219% | 0.241964 | 2.797342 | 0.245777 | 0.876401 | 89.676% |
| 0.5 | 0 | 167322.5 | 13.621% | 5.941050 | 42.289% | 0.165759 | 2.071283 | 0.255979 | 0.856901 | 85.695% |
| 1 | 0 | 178910.6 | 21.490% | 4.240255 | 58.811% | 0.093037 | 1.463082 | 0.270830 | 0.832435 | 81.081% |
| 2 | 0 | 195998.3 | 33.093% | 3.474340 | 66.251% | 0.072420 | 1.168650 | 0.245514 | 0.813643 | 77.605% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
