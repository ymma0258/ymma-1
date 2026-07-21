# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.3 | 0.000% | 7.688893 | 0.000% | 0.229338 | 2.440807 | 0.224030 | 0.882567 | 90.124% |
| 0.25 | 0 | 142373.7 | 6.250% | 4.898962 | 36.285% | 0.150237 | 1.711572 | 0.258144 | 0.867787 | 87.249% |
| 0.5 | 0 | 148153.7 | 10.564% | 3.770778 | 50.958% | 0.110033 | 1.455799 | 0.302413 | 0.842721 | 83.781% |
| 1 | 0 | 156002.9 | 16.422% | 2.441171 | 68.251% | 0.051601 | 1.023294 | 0.338039 | 0.780201 | 74.725% |
| 2 | 0 | 167955.5 | 25.342% | 1.776571 | 76.894% | 0.033236 | 0.576652 | 0.241021 | 0.725530 | 66.096% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
