# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.9 | 0.000% | 8.618701 | 0.000% | 0.262693 | 2.780184 | 0.213269 | 0.869033 | 89.846% |
| 0.25 | 0 | 158255.7 | 7.561% | 7.752975 | 10.045% | 0.213069 | 2.276274 | 0.175180 | 0.869149 | 89.515% |
| 0.5 | 0 | 168848.9 | 14.761% | 5.103319 | 40.788% | 0.135751 | 1.689969 | 0.257770 | 0.841442 | 84.701% |
| 1 | 0 | 180421.9 | 22.627% | 3.668968 | 57.430% | 0.081820 | 1.233713 | 0.264799 | 0.814646 | 79.830% |
| 2 | 0 | 197366.9 | 34.144% | 3.010177 | 65.074% | 0.059017 | 0.947046 | 0.246425 | 0.790362 | 76.120% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
