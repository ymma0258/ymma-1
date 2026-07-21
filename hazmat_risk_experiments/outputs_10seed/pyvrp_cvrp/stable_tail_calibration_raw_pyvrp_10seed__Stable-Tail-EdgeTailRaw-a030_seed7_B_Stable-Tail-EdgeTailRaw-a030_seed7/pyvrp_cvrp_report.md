# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.9 | 0.000% | 10.712661 | 0.000% | 0.326166 | 3.314026 | 0.199925 | 0.882306 | 91.114% |
| 0.25 | 0 | 158021.0 | 7.305% | 8.617871 | 19.554% | 0.250235 | 2.806239 | 0.228795 | 0.880242 | 90.166% |
| 0.5 | 0 | 167258.0 | 13.577% | 5.759536 | 46.236% | 0.153561 | 2.019009 | 0.247115 | 0.855889 | 85.614% |
| 1 | 0 | 178317.3 | 21.087% | 4.200207 | 60.792% | 0.108254 | 1.358153 | 0.238322 | 0.834016 | 81.325% |
| 2 | 0 | 195101.2 | 32.484% | 3.536442 | 66.988% | 0.084364 | 1.141829 | 0.224653 | 0.816594 | 78.224% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
