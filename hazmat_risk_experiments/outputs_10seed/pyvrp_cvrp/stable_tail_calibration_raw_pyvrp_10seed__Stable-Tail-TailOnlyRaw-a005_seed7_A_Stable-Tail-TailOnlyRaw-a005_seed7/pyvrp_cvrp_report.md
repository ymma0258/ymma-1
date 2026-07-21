# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.5 | 0.000% | 9.721112 | 0.000% | 0.328281 | 2.936531 | 0.170101 | 0.873637 | 88.990% |
| 0.25 | 0 | 143383.2 | 6.633% | 5.997316 | 38.306% | 0.173227 | 1.989914 | 0.230922 | 0.857726 | 86.686% |
| 0.5 | 0 | 149366.3 | 11.082% | 4.903868 | 49.554% | 0.142493 | 1.987658 | 0.271809 | 0.845327 | 84.619% |
| 1 | 0 | 158662.8 | 17.996% | 3.305674 | 65.995% | 0.088846 | 1.241232 | 0.288771 | 0.801958 | 77.558% |
| 2 | 0 | 171622.9 | 27.634% | 2.632329 | 72.922% | 0.062554 | 0.834954 | 0.240069 | 0.767849 | 72.332% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
