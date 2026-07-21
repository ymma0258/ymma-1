# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.0 | 0.000% | 8.382810 | 0.000% | 0.232434 | 2.846340 | 0.261949 | 0.884244 | 90.547% |
| 0.25 | 0 | 157001.5 | 6.516% | 6.605477 | 21.202% | 0.162548 | 2.284899 | 0.262092 | 0.876589 | 88.895% |
| 0.5 | 0 | 165301.5 | 12.147% | 4.787059 | 42.894% | 0.121392 | 1.650146 | 0.247111 | 0.853522 | 84.846% |
| 1 | 0 | 175510.1 | 19.073% | 3.125416 | 62.716% | 0.078171 | 1.229722 | 0.301679 | 0.814493 | 78.391% |
| 2 | 0 | 190855.0 | 29.484% | 2.624710 | 68.689% | 0.053039 | 0.977762 | 0.280405 | 0.793610 | 74.721% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
