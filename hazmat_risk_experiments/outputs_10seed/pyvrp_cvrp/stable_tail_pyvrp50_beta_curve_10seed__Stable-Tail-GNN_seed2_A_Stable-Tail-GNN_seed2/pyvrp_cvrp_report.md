# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 8.698255 | 0.000% | 0.272341 | 2.457055 | 0.145302 | 0.877596 | 90.238% |
| 0.25 | 0 | 142356.8 | 6.238% | 6.421599 | 26.174% | 0.194840 | 1.868123 | 0.171326 | 0.874522 | 88.699% |
| 0.5 | 0 | 148680.4 | 10.958% | 5.056976 | 41.862% | 0.149797 | 1.655797 | 0.217882 | 0.861601 | 86.234% |
| 1 | 0 | 158073.2 | 17.967% | 3.477191 | 60.024% | 0.091958 | 1.135270 | 0.282174 | 0.827169 | 80.221% |
| 2 | 0 | 172635.2 | 28.835% | 3.188565 | 63.342% | 0.081796 | 1.169686 | 0.335994 | 0.816234 | 78.387% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
