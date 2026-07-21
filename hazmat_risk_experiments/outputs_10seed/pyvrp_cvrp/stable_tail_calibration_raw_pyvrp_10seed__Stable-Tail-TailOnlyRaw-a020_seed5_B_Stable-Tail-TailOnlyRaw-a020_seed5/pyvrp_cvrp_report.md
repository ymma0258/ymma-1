# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.5 | 0.000% | 8.494953 | 0.000% | 0.261268 | 2.843866 | 0.233844 | 0.878862 | 89.856% |
| 0.25 | 0 | 156622.6 | 6.307% | 7.195095 | 15.302% | 0.188983 | 2.361131 | 0.227961 | 0.876199 | 89.191% |
| 0.5 | 0 | 165048.7 | 12.026% | 5.007077 | 41.058% | 0.120596 | 1.638628 | 0.250987 | 0.849485 | 85.010% |
| 1 | 0 | 175386.3 | 19.043% | 3.737752 | 56.000% | 0.093753 | 1.357917 | 0.301037 | 0.827008 | 80.731% |
| 2 | 0 | 190807.6 | 29.510% | 3.028526 | 64.349% | 0.075331 | 1.000198 | 0.286889 | 0.806203 | 76.895% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
