# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 9.841373 | 0.000% | 0.337105 | 3.125909 | 0.204875 | 0.880277 | 89.990% |
| 0.25 | 0 | 142503.2 | 6.031% | 6.015823 | 38.872% | 0.177614 | 2.004202 | 0.244629 | 0.869553 | 88.031% |
| 0.5 | 0 | 148503.1 | 10.495% | 5.153156 | 47.638% | 0.151820 | 2.020873 | 0.294852 | 0.859238 | 86.284% |
| 1 | 0 | 157603.3 | 17.266% | 3.566574 | 63.759% | 0.099489 | 1.298122 | 0.298541 | 0.823199 | 80.643% |
| 2 | 0 | 172144.1 | 28.085% | 3.042298 | 69.087% | 0.072342 | 1.301879 | 0.356653 | 0.803732 | 77.398% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
