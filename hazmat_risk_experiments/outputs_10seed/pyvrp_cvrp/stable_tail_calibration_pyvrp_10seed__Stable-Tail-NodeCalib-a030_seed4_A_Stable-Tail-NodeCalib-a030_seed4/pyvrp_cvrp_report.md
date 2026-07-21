# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 8.755901 | 0.000% | 0.271354 | 2.470213 | 0.154570 | 0.877738 | 90.005% |
| 0.25 | 0 | 143132.1 | 6.817% | 7.030069 | 19.710% | 0.222092 | 2.134644 | 0.211817 | 0.876502 | 89.438% |
| 0.5 | 0 | 149984.2 | 11.930% | 5.187172 | 40.758% | 0.146445 | 1.742869 | 0.253448 | 0.856747 | 86.189% |
| 1 | 0 | 159488.1 | 19.023% | 3.598015 | 58.908% | 0.082515 | 1.209046 | 0.293596 | 0.820814 | 80.558% |
| 2 | 0 | 174435.3 | 30.177% | 2.875768 | 67.156% | 0.061219 | 1.072577 | 0.359185 | 0.791884 | 76.196% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
