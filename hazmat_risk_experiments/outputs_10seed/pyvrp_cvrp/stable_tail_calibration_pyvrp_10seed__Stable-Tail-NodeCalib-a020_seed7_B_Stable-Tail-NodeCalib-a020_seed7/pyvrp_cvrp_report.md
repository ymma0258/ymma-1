# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147064.0 | 0.000% | 9.887331 | 0.000% | 0.290694 | 3.000110 | 0.189822 | 0.878073 | 90.422% |
| 0.25 | 0 | 157669.2 | 7.211% | 8.155965 | 17.511% | 0.236020 | 2.289917 | 0.175602 | 0.876778 | 89.516% |
| 0.5 | 0 | 167299.5 | 13.760% | 5.881448 | 40.515% | 0.168538 | 2.004942 | 0.261010 | 0.856561 | 85.903% |
| 1 | 0 | 178459.3 | 21.348% | 4.018704 | 59.355% | 0.099928 | 1.233261 | 0.191863 | 0.828366 | 80.437% |
| 2 | 0 | 195383.0 | 32.856% | 3.367589 | 65.940% | 0.067235 | 1.076165 | 0.224239 | 0.808965 | 77.194% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
