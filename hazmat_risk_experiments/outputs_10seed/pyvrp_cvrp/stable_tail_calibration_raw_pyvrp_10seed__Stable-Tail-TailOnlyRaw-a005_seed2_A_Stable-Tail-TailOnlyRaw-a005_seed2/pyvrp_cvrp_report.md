# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 9.002990 | 0.000% | 0.303362 | 2.672078 | 0.173391 | 0.873117 | 88.954% |
| 0.25 | 0 | 142494.6 | 6.024% | 5.996764 | 33.391% | 0.176326 | 2.214868 | 0.290165 | 0.866887 | 87.947% |
| 0.5 | 0 | 148537.7 | 10.521% | 4.851201 | 46.116% | 0.142874 | 1.745160 | 0.260938 | 0.855522 | 85.681% |
| 1 | 0 | 157851.7 | 17.451% | 3.380269 | 62.454% | 0.091818 | 1.385315 | 0.312057 | 0.814890 | 79.550% |
| 2 | 0 | 171783.5 | 27.817% | 2.835777 | 68.502% | 0.068542 | 1.241052 | 0.374247 | 0.792405 | 75.820% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
