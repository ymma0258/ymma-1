# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.937183 | 0.000% | 0.240319 | 2.490944 | 0.209619 | 0.859300 | 89.226% |
| 0.25 | 0 | 156716.9 | 6.660% | 6.818679 | 14.092% | 0.164845 | 2.321425 | 0.227643 | 0.855304 | 88.619% |
| 0.5 | 0 | 165357.3 | 12.541% | 5.590592 | 29.565% | 0.136455 | 1.693593 | 0.193337 | 0.843271 | 86.283% |
| 1 | 0 | 177759.3 | 20.982% | 3.747335 | 52.788% | 0.096099 | 1.323727 | 0.288470 | 0.808506 | 80.472% |
| 2 | 0 | 196109.1 | 33.471% | 2.829497 | 64.351% | 0.065273 | 1.012633 | 0.280707 | 0.769015 | 74.021% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
