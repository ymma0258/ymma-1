# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.905733 | 0.000% | 0.244021 | 2.598277 | 0.223369 | 0.855276 | 88.562% |
| 0.5 | 0 | 165906.0 | 13.068% | 5.196327 | 34.271% | 0.126306 | 1.553904 | 0.153625 | 0.833542 | 84.947% |
| 1 | 0 | 179104.5 | 22.063% | 4.026756 | 49.065% | 0.101343 | 1.261857 | 0.248691 | 0.811339 | 81.263% |
| 1.5 | 0 | 189503.3 | 29.150% | 3.088188 | 60.937% | 0.072523 | 0.949018 | 0.216074 | 0.776882 | 75.883% |
| 2 | 0 | 198253.1 | 35.113% | 2.873798 | 63.649% | 0.065129 | 0.946123 | 0.263442 | 0.764059 | 74.010% |
| 3 | 0 | 214004.8 | 45.848% | 2.707938 | 65.747% | 0.057764 | 0.955011 | 0.295676 | 0.749987 | 71.944% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
