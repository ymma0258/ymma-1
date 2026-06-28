# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.535550 | 0.000% | 0.210085 | 2.330493 | 0.179790 | 0.835901 | 86.235% |
| 0.5 | 0 | 149615.7 | 11.656% | 4.282163 | 43.174% | 0.114189 | 1.967068 | 0.333034 | 0.774286 | 78.535% |
| 1 | 0 | 158711.7 | 18.444% | 3.022258 | 59.893% | 0.066419 | 0.959614 | 0.200004 | 0.704070 | 69.427% |
| 1.5 | 0 | 166618.6 | 24.344% | 2.746362 | 63.555% | 0.054770 | 0.981441 | 0.242987 | 0.673305 | 65.859% |
| 2 | 0 | 173343.0 | 29.363% | 2.342149 | 68.919% | 0.040996 | 0.659368 | 0.155847 | 0.620041 | 59.593% |
| 3 | 0 | 184550.7 | 37.727% | 2.089543 | 72.271% | 0.031604 | 0.593438 | 0.180439 | 0.583752 | 54.997% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
