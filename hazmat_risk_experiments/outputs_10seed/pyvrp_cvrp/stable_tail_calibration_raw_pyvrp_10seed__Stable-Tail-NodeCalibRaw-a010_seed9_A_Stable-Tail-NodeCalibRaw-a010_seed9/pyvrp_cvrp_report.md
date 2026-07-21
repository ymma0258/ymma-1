# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.9 | 0.000% | 8.873741 | 0.000% | 0.289824 | 2.488989 | 0.159740 | 0.869326 | 89.161% |
| 0.25 | 0 | 143354.2 | 6.664% | 5.853692 | 34.034% | 0.166992 | 1.827465 | 0.208793 | 0.857998 | 87.411% |
| 0.5 | 0 | 149712.9 | 11.395% | 4.512811 | 49.144% | 0.118494 | 1.920674 | 0.301772 | 0.831533 | 84.030% |
| 1 | 0 | 158943.8 | 18.264% | 3.036741 | 65.778% | 0.072838 | 1.024935 | 0.230194 | 0.777788 | 76.476% |
| 2 | 0 | 173092.6 | 28.791% | 2.511856 | 71.693% | 0.055122 | 0.753585 | 0.225538 | 0.749240 | 71.989% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
