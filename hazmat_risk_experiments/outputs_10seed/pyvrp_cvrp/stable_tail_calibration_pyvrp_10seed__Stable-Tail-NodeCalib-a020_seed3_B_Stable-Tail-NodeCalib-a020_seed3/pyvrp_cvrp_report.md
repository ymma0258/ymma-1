# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.3 | 0.000% | 6.968116 | 0.000% | 0.190591 | 2.335722 | 0.243832 | 0.869284 | 88.892% |
| 0.25 | 0 | 155362.8 | 5.691% | 5.739926 | 17.626% | 0.142985 | 2.025449 | 0.262659 | 0.863503 | 87.804% |
| 0.5 | 0 | 163348.6 | 11.124% | 4.608864 | 33.858% | 0.115577 | 1.640142 | 0.256047 | 0.849320 | 85.233% |
| 1 | 0 | 174908.1 | 18.987% | 3.384553 | 51.428% | 0.090158 | 1.375005 | 0.323206 | 0.831739 | 81.435% |
| 2 | 0 | 192169.1 | 30.730% | 2.732257 | 60.789% | 0.068042 | 1.218651 | 0.331994 | 0.809528 | 77.530% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
