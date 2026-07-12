# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.8 | 0.000% | 7.428592 | 0.000% | 0.244084 | 2.348157 | 0.229977 | 0.873617 | 87.786% |
| 0.25 | 0 | 142199.5 | 6.068% | 5.623505 | 24.299% | 0.155710 | 1.981777 | 0.273553 | 0.865268 | 85.894% |
| 0.5 | 0 | 147901.2 | 10.321% | 3.954354 | 46.768% | 0.099029 | 1.893637 | 0.357047 | 0.830863 | 80.845% |
| 1 | 0 | 156425.4 | 16.679% | 2.694538 | 63.727% | 0.064769 | 1.045338 | 0.289126 | 0.768406 | 71.911% |
| 2 | 0 | 166999.9 | 24.567% | 1.810817 | 75.624% | 0.035757 | 0.586306 | 0.233534 | 0.698541 | 61.233% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
