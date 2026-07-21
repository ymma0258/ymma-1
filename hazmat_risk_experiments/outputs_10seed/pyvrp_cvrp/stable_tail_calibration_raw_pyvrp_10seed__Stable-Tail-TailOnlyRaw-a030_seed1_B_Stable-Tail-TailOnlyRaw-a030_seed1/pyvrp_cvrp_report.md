# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.8 | 0.000% | 11.074107 | 0.000% | 0.354189 | 3.763824 | 0.247895 | 0.880671 | 91.124% |
| 0.25 | 0 | 156018.7 | 6.185% | 8.970517 | 18.996% | 0.253895 | 2.766440 | 0.220300 | 0.878087 | 89.842% |
| 0.5 | 0 | 164427.0 | 11.908% | 7.939329 | 28.307% | 0.218517 | 2.427988 | 0.221839 | 0.873512 | 88.924% |
| 1 | 0 | 173807.3 | 18.292% | 4.380273 | 60.446% | 0.104810 | 1.628063 | 0.283989 | 0.830305 | 81.328% |
| 2 | 0 | 188148.8 | 28.053% | 3.617014 | 67.338% | 0.072837 | 1.365875 | 0.305660 | 0.811925 | 78.053% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
