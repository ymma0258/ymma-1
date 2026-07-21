# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.2 | 0.000% | 7.635258 | 0.000% | 0.231962 | 2.530497 | 0.225637 | 0.872327 | 88.834% |
| 0.25 | 0 | 156618.8 | 6.401% | 6.569161 | 13.963% | 0.158884 | 2.233694 | 0.242507 | 0.869781 | 88.181% |
| 0.5 | 0 | 165479.0 | 12.420% | 5.570491 | 27.043% | 0.137489 | 1.981898 | 0.292948 | 0.857892 | 86.211% |
| 1 | 0 | 175810.2 | 19.439% | 3.459284 | 54.693% | 0.087797 | 1.243421 | 0.292818 | 0.814231 | 79.140% |
| 2 | 0 | 192039.5 | 30.464% | 2.780815 | 63.579% | 0.066080 | 0.881824 | 0.271678 | 0.787793 | 74.539% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
