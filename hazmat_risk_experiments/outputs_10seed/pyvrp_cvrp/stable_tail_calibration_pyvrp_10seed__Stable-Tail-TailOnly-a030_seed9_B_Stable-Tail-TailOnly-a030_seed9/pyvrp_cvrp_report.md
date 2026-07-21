# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 9.400443 | 0.000% | 0.298256 | 3.007182 | 0.219946 | 0.874221 | 90.350% |
| 0.25 | 0 | 157927.1 | 7.533% | 8.033602 | 14.540% | 0.237693 | 2.452163 | 0.220030 | 0.873944 | 89.999% |
| 0.5 | 0 | 167582.5 | 14.107% | 5.050973 | 46.269% | 0.136039 | 1.609785 | 0.251073 | 0.850624 | 85.274% |
| 1 | 0 | 177821.9 | 21.079% | 3.625439 | 61.433% | 0.080131 | 1.346333 | 0.308058 | 0.817669 | 80.366% |
| 2 | 0 | 194318.5 | 32.312% | 3.089973 | 67.129% | 0.060981 | 0.974626 | 0.241018 | 0.795040 | 76.725% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
