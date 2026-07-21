# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.7 | 0.000% | 6.644695 | 0.000% | 0.202560 | 2.110053 | 0.222859 | 0.868661 | 88.933% |
| 0.25 | 0 | 155642.5 | 5.690% | 5.566068 | 16.233% | 0.136221 | 2.045283 | 0.268081 | 0.863827 | 87.954% |
| 0.5 | 0 | 163082.1 | 10.742% | 4.549936 | 31.525% | 0.113570 | 1.755841 | 0.243807 | 0.853885 | 85.907% |
| 1 | 0 | 174964.1 | 18.810% | 3.417624 | 48.566% | 0.088081 | 1.325288 | 0.288303 | 0.836711 | 82.226% |
| 2 | 0 | 192422.8 | 30.665% | 2.512359 | 62.190% | 0.060847 | 1.086658 | 0.318975 | 0.803195 | 76.522% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
