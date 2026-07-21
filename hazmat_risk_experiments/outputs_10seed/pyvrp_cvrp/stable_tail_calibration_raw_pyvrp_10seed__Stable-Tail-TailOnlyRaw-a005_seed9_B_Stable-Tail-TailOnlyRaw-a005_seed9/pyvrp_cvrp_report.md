# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147264.1 | 0.000% | 9.272592 | 0.000% | 0.290709 | 3.127853 | 0.236946 | 0.872634 | 90.488% |
| 0.25 | 0 | 158224.2 | 7.442% | 7.750750 | 16.412% | 0.224897 | 2.513534 | 0.224376 | 0.870708 | 89.510% |
| 0.5 | 0 | 168593.8 | 14.484% | 5.443290 | 41.297% | 0.144159 | 1.874585 | 0.275623 | 0.851102 | 85.807% |
| 1 | 0 | 179614.8 | 21.968% | 3.437489 | 62.929% | 0.073933 | 1.168758 | 0.271066 | 0.810280 | 78.865% |
| 2 | 0 | 197494.7 | 34.109% | 3.112082 | 66.438% | 0.061166 | 1.007131 | 0.264333 | 0.796648 | 76.722% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
