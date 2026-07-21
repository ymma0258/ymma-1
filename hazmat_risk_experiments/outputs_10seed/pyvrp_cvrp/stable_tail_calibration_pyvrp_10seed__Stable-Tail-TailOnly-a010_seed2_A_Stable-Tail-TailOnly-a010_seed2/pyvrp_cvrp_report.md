# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.7 | 0.000% | 9.245963 | 0.000% | 0.311084 | 3.023551 | 0.208663 | 0.880361 | 90.050% |
| 0.25 | 0 | 142452.9 | 6.099% | 5.892559 | 36.269% | 0.170591 | 2.195825 | 0.289736 | 0.865525 | 87.655% |
| 0.5 | 0 | 148494.0 | 10.598% | 4.910814 | 46.887% | 0.142207 | 1.840115 | 0.290610 | 0.853929 | 85.572% |
| 1 | 0 | 157449.4 | 17.268% | 3.310935 | 64.190% | 0.089098 | 1.336436 | 0.336269 | 0.814970 | 79.434% |
| 2 | 0 | 171608.9 | 27.814% | 3.085788 | 66.626% | 0.081425 | 1.284084 | 0.327498 | 0.804784 | 77.842% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
