# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.5 | 0.000% | 9.368526 | 0.000% | 0.302931 | 2.794198 | 0.173213 | 0.876130 | 89.774% |
| 0.25 | 0 | 143433.2 | 6.670% | 6.575664 | 29.811% | 0.206099 | 2.083434 | 0.238421 | 0.872074 | 88.708% |
| 0.5 | 0 | 150268.5 | 11.753% | 5.204922 | 44.442% | 0.143177 | 1.882232 | 0.279327 | 0.855752 | 86.126% |
| 1 | 0 | 159851.7 | 18.880% | 3.548360 | 62.125% | 0.084500 | 1.072902 | 0.260631 | 0.816262 | 80.057% |
| 2 | 0 | 175090.9 | 30.213% | 2.961865 | 68.385% | 0.062832 | 1.092904 | 0.339638 | 0.795132 | 76.772% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
