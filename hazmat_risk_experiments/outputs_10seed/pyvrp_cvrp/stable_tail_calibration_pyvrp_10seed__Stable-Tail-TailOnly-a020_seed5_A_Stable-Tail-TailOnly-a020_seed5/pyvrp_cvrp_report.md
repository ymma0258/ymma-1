# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.659528 | 0.000% | 0.235541 | 2.265668 | 0.169197 | 0.876677 | 89.336% |
| 0.25 | 0 | 142315.9 | 6.207% | 5.247982 | 31.484% | 0.151826 | 1.922176 | 0.286996 | 0.866482 | 87.104% |
| 0.5 | 0 | 148063.1 | 10.496% | 3.560991 | 53.509% | 0.101729 | 1.260213 | 0.278417 | 0.825669 | 80.915% |
| 1 | 0 | 155291.3 | 15.891% | 2.475509 | 67.681% | 0.063449 | 0.968406 | 0.291125 | 0.769875 | 73.213% |
| 2 | 0 | 166174.2 | 24.012% | 1.924880 | 74.869% | 0.042329 | 0.622659 | 0.233105 | 0.723180 | 66.480% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
