# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.1 | 0.000% | 8.085211 | 0.000% | 0.251120 | 2.443259 | 0.185086 | 0.864186 | 88.347% |
| 0.25 | 0 | 156790.7 | 6.421% | 6.712450 | 16.979% | 0.175041 | 2.149749 | 0.188574 | 0.861361 | 87.713% |
| 0.5 | 0 | 165699.2 | 12.468% | 5.281578 | 34.676% | 0.129485 | 1.874791 | 0.271645 | 0.844322 | 84.809% |
| 1 | 0 | 176312.8 | 19.672% | 3.292929 | 59.272% | 0.078628 | 1.228116 | 0.276126 | 0.792023 | 76.823% |
| 2 | 0 | 192087.4 | 30.379% | 2.612502 | 67.688% | 0.057102 | 0.740254 | 0.189861 | 0.761702 | 71.849% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
