# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.1 | 0.000% | 7.325690 | 0.000% | 0.222836 | 2.371775 | 0.215277 | 0.874036 | 89.014% |
| 0.25 | 0 | 156450.1 | 6.286% | 6.377397 | 12.945% | 0.165990 | 2.230281 | 0.251529 | 0.870871 | 88.445% |
| 0.5 | 0 | 165242.7 | 12.259% | 5.195177 | 29.083% | 0.126171 | 1.686424 | 0.229023 | 0.856239 | 85.944% |
| 1 | 0 | 175264.7 | 19.068% | 3.341354 | 54.389% | 0.082084 | 1.170516 | 0.297337 | 0.818232 | 79.736% |
| 2 | 0 | 191100.1 | 29.826% | 2.619657 | 64.240% | 0.062692 | 0.835520 | 0.268060 | 0.791373 | 74.971% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
