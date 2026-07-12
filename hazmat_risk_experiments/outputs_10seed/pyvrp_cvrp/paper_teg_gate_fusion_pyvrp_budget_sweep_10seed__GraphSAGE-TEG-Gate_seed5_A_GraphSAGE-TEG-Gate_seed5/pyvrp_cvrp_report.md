# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 7.518496 | 0.000% | 0.222572 | 2.222139 | 0.176683 | 0.882892 | 89.951% |
| 0.25 | 0 | 143555.7 | 7.079% | 4.310976 | 42.662% | 0.129819 | 1.384049 | 0.262611 | 0.857540 | 85.380% |
| 0.5 | 0 | 149712.4 | 11.672% | 3.669626 | 51.192% | 0.099045 | 1.388494 | 0.297495 | 0.844822 | 83.312% |
| 1 | 0 | 158322.2 | 18.094% | 2.510778 | 66.605% | 0.054393 | 0.988623 | 0.333159 | 0.796432 | 76.082% |
| 2 | 0 | 170747.1 | 27.362% | 1.912193 | 74.567% | 0.035412 | 0.626489 | 0.277170 | 0.748085 | 68.753% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
