# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 9.269473 | 0.000% | 0.295093 | 2.775879 | 0.173011 | 0.877070 | 89.909% |
| 0.25 | 0 | 143203.0 | 6.604% | 6.430832 | 30.624% | 0.204969 | 2.009982 | 0.227565 | 0.872719 | 88.631% |
| 0.5 | 0 | 150141.9 | 11.770% | 4.942673 | 46.678% | 0.148215 | 1.677530 | 0.263177 | 0.850723 | 85.372% |
| 1 | 0 | 159864.4 | 19.008% | 3.651608 | 60.606% | 0.098846 | 1.357864 | 0.329852 | 0.820680 | 80.690% |
| 2 | 0 | 174696.3 | 30.049% | 2.820421 | 69.573% | 0.065612 | 1.055922 | 0.336829 | 0.789297 | 75.789% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
