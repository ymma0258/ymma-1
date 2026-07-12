# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 6.679216 | 0.000% | 0.209432 | 2.123006 | 0.207597 | 0.873122 | 89.492% |
| 0.25 | 0 | 143108.8 | 6.534% | 5.092278 | 23.759% | 0.141669 | 1.670287 | 0.229760 | 0.869727 | 88.579% |
| 0.5 | 0 | 149340.0 | 11.173% | 3.476890 | 47.945% | 0.096728 | 1.065653 | 0.194536 | 0.838290 | 83.562% |
| 1 | 0 | 158432.3 | 17.941% | 2.509235 | 62.432% | 0.064431 | 0.744671 | 0.216370 | 0.796768 | 77.398% |
| 2 | 0 | 173243.1 | 28.967% | 2.237795 | 66.496% | 0.054649 | 0.725022 | 0.242844 | 0.781986 | 74.508% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
