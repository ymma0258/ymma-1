# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.275491 | 0.000% | 0.291917 | 3.021439 | 0.209019 | 0.877111 | 89.848% |
| 0.25 | 0 | 156955.4 | 6.968% | 7.936215 | 14.439% | 0.222668 | 2.888357 | 0.245169 | 0.874532 | 89.150% |
| 0.5 | 0 | 166202.8 | 13.270% | 5.535419 | 40.322% | 0.144499 | 1.952107 | 0.268667 | 0.850754 | 84.842% |
| 1 | 0 | 176959.2 | 20.601% | 3.963414 | 57.270% | 0.094040 | 1.577595 | 0.340760 | 0.821793 | 80.036% |
| 2 | 0 | 192699.4 | 31.328% | 3.098694 | 66.593% | 0.062068 | 1.406944 | 0.353767 | 0.793335 | 75.444% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
