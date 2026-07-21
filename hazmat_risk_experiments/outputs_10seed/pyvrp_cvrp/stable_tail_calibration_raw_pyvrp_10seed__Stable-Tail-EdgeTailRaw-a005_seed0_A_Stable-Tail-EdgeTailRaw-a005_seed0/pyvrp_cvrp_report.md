# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 8.127788 | 0.000% | 0.252259 | 2.633686 | 0.215882 | 0.884784 | 90.385% |
| 0.25 | 0 | 142499.6 | 6.186% | 4.653838 | 42.742% | 0.139780 | 1.630311 | 0.251652 | 0.861720 | 86.475% |
| 0.5 | 0 | 148345.0 | 10.542% | 3.622529 | 55.430% | 0.105337 | 1.284685 | 0.265103 | 0.833532 | 82.437% |
| 1 | 0 | 156025.5 | 16.265% | 2.346536 | 71.129% | 0.051136 | 0.971747 | 0.297440 | 0.778356 | 74.174% |
| 2 | 0 | 168248.8 | 25.373% | 1.770041 | 78.222% | 0.032125 | 0.564376 | 0.221991 | 0.727162 | 66.378% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
