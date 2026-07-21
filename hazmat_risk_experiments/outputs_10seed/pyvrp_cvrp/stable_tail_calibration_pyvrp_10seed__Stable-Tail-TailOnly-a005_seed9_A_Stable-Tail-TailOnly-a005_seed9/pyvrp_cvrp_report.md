# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 8.725648 | 0.000% | 0.281968 | 2.490877 | 0.167470 | 0.870211 | 89.409% |
| 0.25 | 0 | 142912.0 | 6.388% | 5.891503 | 32.481% | 0.166078 | 1.970075 | 0.237375 | 0.858875 | 87.665% |
| 0.5 | 0 | 149536.4 | 11.319% | 4.301979 | 50.697% | 0.108989 | 1.523539 | 0.247765 | 0.827936 | 83.240% |
| 1 | 0 | 158272.2 | 17.822% | 2.862132 | 67.199% | 0.067207 | 1.020880 | 0.265533 | 0.769156 | 75.210% |
| 2 | 0 | 172295.9 | 28.262% | 2.643724 | 69.702% | 0.060292 | 0.814796 | 0.219585 | 0.759852 | 73.500% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
