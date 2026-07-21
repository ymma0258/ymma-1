# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134531.1 | 0.000% | 8.733669 | 0.000% | 0.279867 | 2.542353 | 0.163901 | 0.868043 | 88.676% |
| 0.25 | 0 | 143422.2 | 6.609% | 4.978374 | 42.998% | 0.141311 | 1.655548 | 0.262930 | 0.845117 | 85.071% |
| 0.5 | 0 | 149803.3 | 11.352% | 4.153987 | 52.437% | 0.122101 | 1.530940 | 0.286007 | 0.822297 | 82.235% |
| 1 | 0 | 159052.2 | 18.227% | 2.935585 | 66.388% | 0.078744 | 1.088289 | 0.317625 | 0.778288 | 75.774% |
| 2 | 0 | 173280.6 | 28.803% | 2.286689 | 73.818% | 0.052349 | 0.867470 | 0.304052 | 0.729676 | 69.117% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
