# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.0 | 0.000% | 7.588008 | 0.000% | 0.228813 | 2.362671 | 0.209196 | 0.860645 | 87.881% |
| 0.25 | 0 | 157017.4 | 6.623% | 6.517266 | 14.111% | 0.168156 | 2.194681 | 0.222430 | 0.855738 | 87.191% |
| 0.5 | 0 | 165550.3 | 12.417% | 4.765165 | 37.201% | 0.114078 | 1.473650 | 0.219024 | 0.835448 | 83.478% |
| 1 | 0 | 176331.2 | 19.738% | 2.993705 | 60.547% | 0.070003 | 1.003703 | 0.222254 | 0.779855 | 75.059% |
| 2 | 0 | 191374.5 | 29.953% | 2.530187 | 66.655% | 0.055836 | 0.735185 | 0.202734 | 0.755956 | 71.140% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
