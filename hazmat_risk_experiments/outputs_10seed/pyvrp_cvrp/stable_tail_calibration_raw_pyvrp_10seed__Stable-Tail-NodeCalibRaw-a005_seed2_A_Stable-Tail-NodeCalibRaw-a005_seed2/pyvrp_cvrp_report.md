# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 9.089295 | 0.000% | 0.298116 | 2.911084 | 0.205757 | 0.876831 | 89.523% |
| 0.25 | 0 | 142655.2 | 6.144% | 5.893910 | 35.155% | 0.171795 | 1.901046 | 0.225229 | 0.863881 | 87.642% |
| 0.5 | 0 | 148771.0 | 10.694% | 4.734929 | 47.907% | 0.136908 | 1.752110 | 0.257080 | 0.850058 | 85.121% |
| 1 | 0 | 157952.2 | 17.526% | 3.296955 | 63.727% | 0.091222 | 1.158849 | 0.297907 | 0.812250 | 79.233% |
| 2 | 0 | 172266.7 | 28.177% | 2.905851 | 68.030% | 0.070980 | 1.148465 | 0.326491 | 0.795504 | 76.461% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
