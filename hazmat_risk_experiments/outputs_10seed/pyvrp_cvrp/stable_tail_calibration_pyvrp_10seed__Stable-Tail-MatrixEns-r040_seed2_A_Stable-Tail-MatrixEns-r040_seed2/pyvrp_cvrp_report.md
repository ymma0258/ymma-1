# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 5.191900 | 0.000% | 0.164697 | 1.512474 | 0.171554 | 0.876745 | 89.660% |
| 0.25 | 0 | 142298.6 | 6.194% | 3.533385 | 31.944% | 0.104353 | 1.206089 | 0.253256 | 0.866257 | 87.703% |
| 0.5 | 0 | 148383.3 | 10.735% | 2.847988 | 45.146% | 0.085053 | 0.882737 | 0.207441 | 0.856103 | 85.504% |
| 1 | 0 | 157301.4 | 17.391% | 2.001180 | 61.456% | 0.055061 | 0.746830 | 0.319948 | 0.816378 | 79.705% |
| 2 | 0 | 171509.2 | 27.994% | 1.697942 | 67.296% | 0.039648 | 0.715564 | 0.365183 | 0.793031 | 75.951% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
