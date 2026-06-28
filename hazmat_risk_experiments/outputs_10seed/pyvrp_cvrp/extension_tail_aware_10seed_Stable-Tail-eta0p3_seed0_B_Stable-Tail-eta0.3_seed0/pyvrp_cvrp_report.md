# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.738138 | 0.000% | 0.203838 | 3.217207 | 0.229187 | 0.884425 | 90.632% |
| 1 | 0 | 176311.2 | 20.160% | 3.590161 | 63.133% | 0.071615 | 1.310841 | 0.295415 | 0.820757 | 79.006% |
| 2 | 0 | 190410.1 | 29.768% | 2.963995 | 69.563% | 0.056354 | 1.225721 | 0.310147 | 0.795342 | 74.357% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
