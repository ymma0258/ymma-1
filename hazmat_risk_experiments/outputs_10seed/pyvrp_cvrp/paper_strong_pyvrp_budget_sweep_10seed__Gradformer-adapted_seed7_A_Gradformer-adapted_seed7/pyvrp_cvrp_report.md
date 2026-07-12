# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 8.152368 | 0.000% | 0.251193 | 2.142791 | 0.131218 | 0.851599 | 88.904% |
| 0.25 | 0 | 142946.4 | 6.625% | 6.644498 | 18.496% | 0.196280 | 2.149715 | 0.213596 | 0.852430 | 88.255% |
| 0.5 | 0 | 149866.9 | 11.787% | 4.461569 | 45.273% | 0.127105 | 1.479203 | 0.206849 | 0.814651 | 82.945% |
| 1 | 0 | 160976.6 | 20.074% | 3.756736 | 53.918% | 0.105577 | 1.283118 | 0.256782 | 0.801345 | 80.206% |
| 2 | 0 | 177278.2 | 32.233% | 2.703341 | 66.840% | 0.065342 | 0.959500 | 0.310788 | 0.744355 | 72.224% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
