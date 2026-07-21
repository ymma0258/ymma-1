# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147063.9 | 0.000% | 8.088418 | 0.000% | 0.244603 | 2.399682 | 0.177185 | 0.878619 | 90.658% |
| 0.25 | 0 | 157751.1 | 7.267% | 6.562048 | 18.871% | 0.190299 | 2.165843 | 0.240076 | 0.876983 | 89.517% |
| 0.5 | 0 | 167254.1 | 13.729% | 4.909430 | 39.303% | 0.135577 | 1.739541 | 0.260256 | 0.860190 | 86.319% |
| 1 | 0 | 178670.1 | 21.491% | 3.371731 | 58.314% | 0.088068 | 1.140778 | 0.256652 | 0.833091 | 81.335% |
| 2 | 0 | 195286.9 | 32.791% | 2.782173 | 65.603% | 0.069054 | 0.873911 | 0.212333 | 0.812891 | 77.755% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
