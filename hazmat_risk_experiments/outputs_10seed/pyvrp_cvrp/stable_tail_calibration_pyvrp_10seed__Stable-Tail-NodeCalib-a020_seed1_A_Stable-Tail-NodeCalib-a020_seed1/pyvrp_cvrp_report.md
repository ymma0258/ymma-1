# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 9.041101 | 0.000% | 0.294157 | 2.527400 | 0.153172 | 0.871922 | 89.529% |
| 0.25 | 0 | 141864.3 | 5.870% | 6.319441 | 30.103% | 0.194446 | 1.781989 | 0.179031 | 0.862350 | 87.539% |
| 0.5 | 0 | 147667.7 | 10.201% | 4.566300 | 49.494% | 0.111509 | 1.549036 | 0.207144 | 0.838318 | 83.440% |
| 1 | 0 | 156242.0 | 16.600% | 3.320730 | 63.271% | 0.077075 | 1.065982 | 0.210686 | 0.796895 | 77.387% |
| 2 | 0 | 168880.6 | 26.032% | 2.791473 | 69.125% | 0.058714 | 0.845917 | 0.228961 | 0.772946 | 73.433% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
