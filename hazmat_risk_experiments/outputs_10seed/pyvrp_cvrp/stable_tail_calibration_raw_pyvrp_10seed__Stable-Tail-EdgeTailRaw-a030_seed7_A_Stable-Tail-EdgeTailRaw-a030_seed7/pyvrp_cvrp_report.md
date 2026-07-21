# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 9.848098 | 0.000% | 0.322016 | 2.693427 | 0.163809 | 0.878417 | 89.991% |
| 0.25 | 0 | 143409.8 | 6.705% | 5.874601 | 40.348% | 0.172887 | 1.925424 | 0.218619 | 0.858639 | 86.534% |
| 0.5 | 0 | 149315.6 | 11.100% | 4.889863 | 50.347% | 0.141251 | 1.953776 | 0.284216 | 0.844403 | 84.224% |
| 1 | 0 | 158540.7 | 17.964% | 3.302409 | 66.467% | 0.087759 | 1.371064 | 0.320277 | 0.800910 | 77.378% |
| 2 | 0 | 170802.4 | 27.087% | 2.629179 | 73.303% | 0.063499 | 0.833510 | 0.232978 | 0.766154 | 71.986% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
