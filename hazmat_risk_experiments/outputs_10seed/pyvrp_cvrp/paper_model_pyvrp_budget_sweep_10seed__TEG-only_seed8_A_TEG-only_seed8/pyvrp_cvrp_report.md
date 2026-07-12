# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.7 | 0.000% | 8.630549 | 0.000% | 0.256805 | 2.680727 | 0.181761 | 0.842396 | 86.792% |
| 0.25 | 0 | 143530.6 | 7.007% | 6.028804 | 30.146% | 0.160331 | 1.839595 | 0.196128 | 0.816760 | 83.893% |
| 0.5 | 0 | 150266.8 | 12.029% | 4.981310 | 42.283% | 0.123045 | 1.699814 | 0.237504 | 0.793969 | 80.681% |
| 1 | 0 | 160471.8 | 19.637% | 3.598664 | 58.303% | 0.080459 | 1.159210 | 0.243300 | 0.733997 | 73.313% |
| 2 | 0 | 176346.9 | 31.473% | 3.056878 | 64.581% | 0.061900 | 0.986280 | 0.214034 | 0.691344 | 67.869% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
