# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 9.801180 | 0.000% | 0.306416 | 3.415811 | 0.255200 | 0.873239 | 89.863% |
| 0.25 | 0 | 155917.9 | 6.069% | 7.740477 | 21.025% | 0.240993 | 2.595595 | 0.247155 | 0.866725 | 88.177% |
| 0.5 | 0 | 163970.6 | 11.547% | 6.787062 | 30.753% | 0.194129 | 1.969025 | 0.192836 | 0.860852 | 87.012% |
| 1 | 0 | 173688.6 | 18.158% | 3.750478 | 61.734% | 0.080459 | 1.328330 | 0.274272 | 0.810721 | 78.366% |
| 2 | 0 | 187482.7 | 27.542% | 3.205281 | 67.297% | 0.062675 | 1.192536 | 0.266689 | 0.792325 | 75.193% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
