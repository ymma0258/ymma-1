# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.325140 | 0.000% | 0.252710 | 2.391842 | 0.135789 | 0.848338 | 87.650% |
| 0.5 | 0 | 151029.9 | 12.711% | 5.166619 | 37.940% | 0.146012 | 2.024313 | 0.294290 | 0.810381 | 82.354% |
| 1 | 0 | 161900.6 | 20.824% | 3.704421 | 55.503% | 0.092309 | 1.219703 | 0.265453 | 0.757616 | 75.247% |
| 1.5 | 0 | 171183.0 | 27.751% | 3.611637 | 56.618% | 0.083260 | 1.179837 | 0.249000 | 0.752441 | 74.524% |
| 2 | 0 | 179860.9 | 34.227% | 3.140962 | 62.271% | 0.063639 | 1.229404 | 0.286981 | 0.716143 | 70.034% |
| 3 | 0 | 194192.9 | 44.923% | 2.776134 | 66.654% | 0.051889 | 1.202195 | 0.346096 | 0.689468 | 66.556% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
