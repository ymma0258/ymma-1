# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.5 | 0.000% | 7.311639 | 0.000% | 0.223136 | 2.160934 | 0.174596 | 0.860220 | 88.643% |
| 0.25 | 0 | 143135.2 | 6.554% | 5.426594 | 25.781% | 0.148150 | 1.568804 | 0.184739 | 0.847610 | 86.422% |
| 0.5 | 0 | 149434.1 | 11.243% | 4.094760 | 43.997% | 0.113829 | 1.464946 | 0.235643 | 0.824397 | 82.657% |
| 1 | 0 | 159236.4 | 18.540% | 3.369402 | 53.917% | 0.093463 | 1.092080 | 0.216200 | 0.800665 | 78.784% |
| 2 | 0 | 172079.5 | 28.101% | 2.045032 | 72.030% | 0.045466 | 0.623222 | 0.234642 | 0.708397 | 65.103% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
