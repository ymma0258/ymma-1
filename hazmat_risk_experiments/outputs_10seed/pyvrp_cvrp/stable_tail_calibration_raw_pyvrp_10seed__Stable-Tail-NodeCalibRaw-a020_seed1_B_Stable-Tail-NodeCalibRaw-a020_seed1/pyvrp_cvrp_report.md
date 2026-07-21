# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.4 | 0.000% | 9.886117 | 0.000% | 0.313373 | 3.517035 | 0.271629 | 0.872801 | 89.982% |
| 0.25 | 0 | 156455.2 | 6.193% | 8.149593 | 17.565% | 0.254528 | 2.739680 | 0.228750 | 0.870226 | 88.864% |
| 0.5 | 0 | 164259.2 | 11.490% | 6.877046 | 30.437% | 0.196656 | 2.198057 | 0.236025 | 0.861082 | 87.180% |
| 1 | 0 | 174427.7 | 18.392% | 3.870427 | 60.850% | 0.091349 | 1.301287 | 0.263389 | 0.815026 | 79.028% |
| 2 | 0 | 188167.8 | 27.718% | 3.312046 | 66.498% | 0.065700 | 1.135707 | 0.241709 | 0.795713 | 75.852% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
