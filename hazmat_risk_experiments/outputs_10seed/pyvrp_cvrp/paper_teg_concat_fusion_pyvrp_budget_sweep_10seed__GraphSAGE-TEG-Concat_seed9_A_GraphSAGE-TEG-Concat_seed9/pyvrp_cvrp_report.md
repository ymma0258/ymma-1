# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 8.841508 | 0.000% | 0.278606 | 2.725800 | 0.182313 | 0.885914 | 90.318% |
| 0.25 | 0 | 143897.7 | 7.068% | 5.321610 | 39.811% | 0.147627 | 1.890195 | 0.273136 | 0.870263 | 87.040% |
| 0.5 | 0 | 150761.6 | 12.175% | 3.875323 | 56.169% | 0.095559 | 1.371804 | 0.270415 | 0.838246 | 82.153% |
| 1 | 0 | 159709.6 | 18.833% | 2.971245 | 66.394% | 0.070107 | 0.913536 | 0.242518 | 0.805516 | 77.296% |
| 2 | 0 | 173594.0 | 29.164% | 2.208250 | 75.024% | 0.046915 | 0.894256 | 0.303229 | 0.759146 | 69.876% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
