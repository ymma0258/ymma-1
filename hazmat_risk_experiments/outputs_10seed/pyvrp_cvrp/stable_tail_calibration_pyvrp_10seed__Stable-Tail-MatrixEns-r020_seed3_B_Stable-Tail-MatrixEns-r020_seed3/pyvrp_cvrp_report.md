# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 5.618259 | 0.000% | 0.175450 | 1.912332 | 0.242004 | 0.869272 | 88.961% |
| 0.25 | 0 | 155217.0 | 5.640% | 4.546400 | 19.078% | 0.113594 | 1.604396 | 0.260881 | 0.863957 | 87.845% |
| 0.5 | 0 | 163051.7 | 10.972% | 3.681171 | 34.478% | 0.093196 | 1.430715 | 0.274078 | 0.850502 | 85.314% |
| 1 | 0 | 174862.0 | 19.010% | 2.890095 | 48.559% | 0.072919 | 1.157196 | 0.301315 | 0.838111 | 82.483% |
| 2 | 0 | 192105.7 | 30.746% | 2.153019 | 61.678% | 0.053819 | 0.836541 | 0.291348 | 0.807513 | 77.146% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
