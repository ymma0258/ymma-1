# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.9 | 0.000% | 6.450410 | 0.000% | 0.206237 | 1.826422 | 0.162106 | 0.874378 | 89.849% |
| 0.25 | 0 | 141943.6 | 5.877% | 4.581745 | 28.970% | 0.143449 | 1.477845 | 0.223863 | 0.868618 | 88.119% |
| 0.5 | 0 | 147704.0 | 10.174% | 3.322878 | 48.486% | 0.091537 | 1.136867 | 0.212485 | 0.842172 | 84.096% |
| 1 | 0 | 156425.0 | 16.679% | 2.291918 | 64.469% | 0.052611 | 0.675013 | 0.185026 | 0.798218 | 77.569% |
| 2 | 0 | 168749.1 | 25.871% | 1.930860 | 70.066% | 0.038184 | 0.595141 | 0.224795 | 0.775913 | 73.744% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
