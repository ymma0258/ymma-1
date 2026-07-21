# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.7 | 0.000% | 10.314876 | 0.000% | 0.328571 | 3.639681 | 0.268599 | 0.874962 | 90.261% |
| 0.25 | 0 | 156242.1 | 5.953% | 8.410040 | 18.467% | 0.244166 | 2.565288 | 0.214548 | 0.873675 | 89.205% |
| 0.5 | 0 | 164372.7 | 11.467% | 6.777504 | 34.294% | 0.181628 | 2.202939 | 0.232011 | 0.862178 | 87.044% |
| 1 | 0 | 174487.2 | 18.326% | 4.126111 | 59.998% | 0.100665 | 1.375903 | 0.262653 | 0.820917 | 80.139% |
| 2 | 0 | 187879.6 | 27.407% | 3.419399 | 66.850% | 0.068484 | 1.199645 | 0.259633 | 0.799534 | 76.396% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
