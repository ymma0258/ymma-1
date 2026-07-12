# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.5 | 0.000% | 8.633116 | 0.000% | 0.266707 | 2.685318 | 0.181599 | 0.865713 | 88.946% |
| 0.25 | 0 | 144740.6 | 7.749% | 5.951240 | 31.065% | 0.183539 | 1.821647 | 0.196180 | 0.852108 | 87.159% |
| 0.5 | 0 | 152471.7 | 13.504% | 4.838145 | 43.958% | 0.139909 | 1.415675 | 0.201013 | 0.836592 | 84.629% |
| 1 | 0 | 163618.3 | 21.802% | 3.515828 | 59.275% | 0.079878 | 1.241813 | 0.302467 | 0.797554 | 79.003% |
| 2 | 0 | 182165.4 | 35.609% | 2.701224 | 68.711% | 0.058268 | 1.035935 | 0.341574 | 0.754118 | 72.747% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
