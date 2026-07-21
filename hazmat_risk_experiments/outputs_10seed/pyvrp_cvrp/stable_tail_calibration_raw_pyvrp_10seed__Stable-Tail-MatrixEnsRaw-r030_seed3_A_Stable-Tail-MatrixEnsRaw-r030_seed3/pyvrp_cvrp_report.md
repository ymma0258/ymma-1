# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.0 | 0.000% | 4.864934 | 0.000% | 0.143860 | 1.558310 | 0.200625 | 0.873706 | 89.126% |
| 0.25 | 0 | 141673.9 | 5.571% | 3.454010 | 29.002% | 0.100278 | 1.044343 | 0.211988 | 0.857825 | 86.833% |
| 0.5 | 0 | 147171.3 | 9.667% | 2.553115 | 47.520% | 0.074679 | 0.922288 | 0.271257 | 0.832718 | 83.019% |
| 1 | 0 | 155135.2 | 15.602% | 1.666989 | 65.735% | 0.042812 | 0.515076 | 0.236167 | 0.770867 | 74.457% |
| 2 | 0 | 166814.5 | 24.305% | 1.547286 | 68.195% | 0.038042 | 0.491540 | 0.264805 | 0.757704 | 72.416% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
