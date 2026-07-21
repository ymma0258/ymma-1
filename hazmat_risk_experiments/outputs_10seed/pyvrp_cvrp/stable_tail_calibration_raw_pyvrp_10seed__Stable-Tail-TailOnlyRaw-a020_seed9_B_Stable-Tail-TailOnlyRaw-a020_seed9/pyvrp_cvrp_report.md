# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.2 | 0.000% | 10.000238 | 0.000% | 0.316757 | 3.334434 | 0.235960 | 0.876797 | 91.161% |
| 0.25 | 0 | 158650.2 | 7.634% | 8.566905 | 14.333% | 0.255801 | 2.793041 | 0.236673 | 0.874649 | 90.420% |
| 0.5 | 0 | 168571.2 | 14.365% | 5.816537 | 41.836% | 0.155265 | 1.895321 | 0.254480 | 0.861045 | 86.916% |
| 1 | 0 | 179469.6 | 21.759% | 3.831186 | 61.689% | 0.082366 | 1.239736 | 0.242595 | 0.823327 | 80.817% |
| 2 | 0 | 197488.7 | 33.984% | 3.381004 | 66.191% | 0.071948 | 1.084493 | 0.244162 | 0.809393 | 78.506% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
