# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 9.446972 | 0.000% | 0.270990 | 3.014888 | 0.205173 | 0.849479 | 88.339% |
| 0.25 | 0 | 158193.4 | 7.714% | 8.180389 | 13.407% | 0.201639 | 2.716408 | 0.227649 | 0.849278 | 88.534% |
| 0.5 | 0 | 169080.0 | 15.127% | 6.530664 | 30.870% | 0.171443 | 2.147633 | 0.219875 | 0.835658 | 85.889% |
| 1 | 0 | 183474.2 | 24.928% | 5.009839 | 46.969% | 0.132593 | 1.734443 | 0.262416 | 0.811830 | 82.157% |
| 2 | 0 | 205859.7 | 40.170% | 3.835318 | 59.402% | 0.084130 | 1.424938 | 0.329444 | 0.777404 | 76.527% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
