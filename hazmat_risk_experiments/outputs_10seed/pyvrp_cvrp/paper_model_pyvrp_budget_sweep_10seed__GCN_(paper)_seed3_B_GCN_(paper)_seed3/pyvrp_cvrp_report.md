# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 7.839334 | 0.000% | 0.236072 | 2.463739 | 0.211689 | 0.853883 | 88.483% |
| 0.25 | 0 | 157205.9 | 6.945% | 6.515966 | 16.881% | 0.158535 | 2.234408 | 0.226256 | 0.848529 | 87.918% |
| 0.5 | 0 | 166955.0 | 13.577% | 5.242264 | 33.129% | 0.132532 | 1.638920 | 0.208841 | 0.835628 | 85.469% |
| 1 | 0 | 181365.5 | 23.380% | 4.122171 | 47.417% | 0.108620 | 1.319221 | 0.231896 | 0.815064 | 81.930% |
| 2 | 0 | 202134.0 | 37.509% | 3.080646 | 60.703% | 0.074755 | 0.996900 | 0.257363 | 0.780618 | 76.353% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
