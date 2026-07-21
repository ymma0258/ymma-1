# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 5.157872 | 0.000% | 0.157847 | 1.507643 | 0.167574 | 0.873479 | 88.919% |
| 0.25 | 0 | 142421.1 | 6.286% | 3.756843 | 27.163% | 0.106673 | 1.186644 | 0.220383 | 0.863157 | 86.880% |
| 0.5 | 0 | 147950.7 | 10.413% | 2.557496 | 50.416% | 0.074579 | 0.992470 | 0.310528 | 0.828207 | 81.731% |
| 1 | 0 | 155969.8 | 16.397% | 1.708059 | 66.884% | 0.043372 | 0.688986 | 0.299920 | 0.767936 | 73.058% |
| 2 | 0 | 167227.5 | 24.799% | 1.325757 | 74.296% | 0.028877 | 0.433062 | 0.220724 | 0.716935 | 65.636% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
