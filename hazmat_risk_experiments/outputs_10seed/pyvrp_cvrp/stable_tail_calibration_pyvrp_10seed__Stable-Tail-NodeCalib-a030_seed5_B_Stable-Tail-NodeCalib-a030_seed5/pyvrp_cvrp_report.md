# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.752438 | 0.000% | 0.241236 | 2.534007 | 0.219417 | 0.874384 | 88.944% |
| 0.25 | 0 | 156112.0 | 6.249% | 6.691325 | 13.687% | 0.160096 | 2.264710 | 0.248839 | 0.871703 | 88.443% |
| 0.5 | 0 | 164500.2 | 11.958% | 5.149867 | 33.571% | 0.127345 | 1.674779 | 0.233706 | 0.849015 | 84.904% |
| 1 | 0 | 174856.3 | 19.006% | 3.443698 | 55.579% | 0.088073 | 1.253111 | 0.309856 | 0.816324 | 79.247% |
| 2 | 0 | 190701.4 | 29.790% | 2.781528 | 64.121% | 0.067436 | 0.883458 | 0.277828 | 0.793110 | 75.224% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
