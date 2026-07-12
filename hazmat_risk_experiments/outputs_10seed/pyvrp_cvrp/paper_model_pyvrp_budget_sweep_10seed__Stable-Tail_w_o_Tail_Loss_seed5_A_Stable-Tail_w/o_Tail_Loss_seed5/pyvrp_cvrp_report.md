# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 7.119500 | 0.000% | 0.223592 | 2.052865 | 0.173365 | 0.875147 | 90.017% |
| 0.25 | 0 | 143291.1 | 6.670% | 5.152450 | 27.629% | 0.153362 | 1.673877 | 0.236151 | 0.874587 | 88.750% |
| 0.5 | 0 | 150148.2 | 11.774% | 3.797254 | 46.664% | 0.114312 | 1.250925 | 0.209094 | 0.848465 | 84.792% |
| 1 | 0 | 159867.3 | 19.010% | 2.713389 | 61.888% | 0.071220 | 0.882893 | 0.254791 | 0.815308 | 79.255% |
| 2 | 0 | 174773.0 | 30.106% | 2.228408 | 68.700% | 0.043790 | 0.730511 | 0.251795 | 0.791525 | 75.014% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
