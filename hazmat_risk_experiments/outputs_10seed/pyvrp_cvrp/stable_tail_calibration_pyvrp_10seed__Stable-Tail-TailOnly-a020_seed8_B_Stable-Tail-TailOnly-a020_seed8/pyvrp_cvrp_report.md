# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 7.777207 | 0.000% | 0.240421 | 2.370541 | 0.197023 | 0.863235 | 88.108% |
| 0.25 | 0 | 155916.9 | 6.068% | 6.216365 | 20.069% | 0.144705 | 2.115558 | 0.230641 | 0.855133 | 86.754% |
| 0.5 | 0 | 164439.3 | 11.866% | 4.658748 | 40.097% | 0.114892 | 1.385740 | 0.193998 | 0.835052 | 83.366% |
| 1 | 0 | 174943.1 | 19.011% | 3.134645 | 59.694% | 0.074930 | 1.115773 | 0.230690 | 0.786383 | 76.062% |
| 2 | 0 | 188862.3 | 28.480% | 2.444698 | 68.566% | 0.053143 | 0.723910 | 0.214405 | 0.751449 | 70.493% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
