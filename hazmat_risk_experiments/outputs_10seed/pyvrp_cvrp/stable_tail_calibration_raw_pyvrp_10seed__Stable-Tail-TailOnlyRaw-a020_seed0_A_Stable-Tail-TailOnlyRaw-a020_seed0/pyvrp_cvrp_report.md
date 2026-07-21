# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 8.287734 | 0.000% | 0.257042 | 2.442523 | 0.188562 | 0.885770 | 90.762% |
| 0.25 | 0 | 141997.1 | 5.759% | 4.935102 | 40.453% | 0.150570 | 1.599653 | 0.231114 | 0.868351 | 87.296% |
| 0.5 | 0 | 147663.8 | 9.980% | 4.077551 | 50.800% | 0.122541 | 1.472848 | 0.278292 | 0.850332 | 84.929% |
| 1 | 0 | 155321.8 | 15.683% | 2.536969 | 69.389% | 0.061329 | 1.115357 | 0.337240 | 0.792258 | 76.154% |
| 2 | 0 | 166725.8 | 24.177% | 1.879556 | 77.321% | 0.034869 | 0.631622 | 0.234812 | 0.741396 | 68.381% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
