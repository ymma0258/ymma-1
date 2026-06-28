# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.904615 | 0.000% | 0.272518 | 2.788138 | 0.187097 | 0.841212 | 87.122% |
| 0.5 | 0 | 168023.5 | 14.511% | 5.112388 | 42.587% | 0.124792 | 1.681609 | 0.238877 | 0.780903 | 78.996% |
| 1 | 0 | 181548.4 | 23.729% | 4.293602 | 51.782% | 0.084585 | 1.414243 | 0.244848 | 0.752265 | 75.303% |
| 1.5 | 0 | 192398.4 | 31.123% | 3.509879 | 60.584% | 0.066015 | 1.393575 | 0.290800 | 0.713612 | 69.893% |
| 2 | 0 | 201962.8 | 37.642% | 3.356982 | 62.301% | 0.064322 | 1.327838 | 0.303367 | 0.701975 | 68.386% |
| 3 | 0 | 220163.0 | 50.045% | 3.295975 | 62.986% | 0.061103 | 1.343563 | 0.294835 | 0.699035 | 68.057% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
