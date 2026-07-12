# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134597.7 | 0.000% | 8.033897 | 0.000% | 0.271191 | 2.359729 | 0.160254 | 0.874289 | 88.345% |
| 0.25 | 0 | 142091.5 | 5.568% | 5.257987 | 34.552% | 0.143786 | 1.943557 | 0.276497 | 0.868237 | 86.318% |
| 0.5 | 0 | 147027.6 | 9.235% | 3.700955 | 53.933% | 0.089807 | 1.558070 | 0.279969 | 0.827583 | 80.697% |
| 1 | 0 | 155524.1 | 15.547% | 2.321290 | 71.106% | 0.050576 | 0.667303 | 0.168450 | 0.753463 | 69.653% |
| 2 | 0 | 167021.5 | 24.089% | 1.992771 | 75.195% | 0.041482 | 0.567861 | 0.174285 | 0.718858 | 64.576% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
