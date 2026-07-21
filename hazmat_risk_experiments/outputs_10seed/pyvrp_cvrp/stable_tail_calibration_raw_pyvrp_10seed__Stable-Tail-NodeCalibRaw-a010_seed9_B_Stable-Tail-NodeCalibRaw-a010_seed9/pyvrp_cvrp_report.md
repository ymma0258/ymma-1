# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.2 | 0.000% | 9.128905 | 0.000% | 0.284998 | 2.943060 | 0.223362 | 0.869734 | 89.971% |
| 0.25 | 0 | 158377.9 | 7.450% | 7.706894 | 15.577% | 0.227856 | 2.360475 | 0.198858 | 0.870656 | 89.484% |
| 0.5 | 0 | 167937.8 | 13.936% | 4.965972 | 45.602% | 0.128057 | 1.659851 | 0.264162 | 0.845179 | 84.690% |
| 1 | 0 | 179776.3 | 21.967% | 3.520067 | 61.440% | 0.074602 | 1.093650 | 0.234651 | 0.810190 | 79.117% |
| 2 | 0 | 197213.0 | 33.797% | 3.107779 | 65.957% | 0.062853 | 0.968617 | 0.225718 | 0.794767 | 76.661% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
