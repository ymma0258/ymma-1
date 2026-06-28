# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 11.218722 | 0.000% | 0.179747 | 3.788911 | 0.247554 | 0.884069 | 90.177% |
| 1 | 0 | 174482.1 | 18.913% | 3.680128 | 67.197% | 0.041928 | 1.307291 | 0.270547 | 0.799850 | 74.184% |
| 2 | 0 | 188661.8 | 28.577% | 3.528359 | 68.549% | 0.040848 | 1.298790 | 0.293427 | 0.796422 | 73.706% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
