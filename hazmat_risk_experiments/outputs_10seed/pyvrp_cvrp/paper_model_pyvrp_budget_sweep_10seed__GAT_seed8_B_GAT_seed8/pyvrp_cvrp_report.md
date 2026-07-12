# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.4 | 0.000% | 8.397486 | 0.000% | 0.250264 | 2.695544 | 0.215042 | 0.850715 | 88.656% |
| 0.25 | 0 | 158392.8 | 7.606% | 7.390009 | 11.997% | 0.211657 | 2.403779 | 0.221231 | 0.851934 | 88.585% |
| 0.5 | 0 | 169033.9 | 14.835% | 5.913245 | 29.583% | 0.154714 | 1.843282 | 0.219448 | 0.838010 | 86.014% |
| 1 | 0 | 183380.8 | 24.582% | 4.238964 | 49.521% | 0.094114 | 1.452701 | 0.277450 | 0.807072 | 81.056% |
| 2 | 0 | 204165.8 | 38.702% | 3.192233 | 61.986% | 0.065805 | 1.027710 | 0.285663 | 0.768674 | 74.820% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
