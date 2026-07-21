# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.7 | 0.000% | 9.574344 | 0.000% | 0.325090 | 2.944789 | 0.198902 | 0.881537 | 90.221% |
| 0.25 | 0 | 142302.5 | 5.987% | 6.295394 | 34.247% | 0.183808 | 2.029629 | 0.227560 | 0.871620 | 88.504% |
| 0.5 | 0 | 148514.2 | 10.613% | 4.929801 | 48.510% | 0.145607 | 1.750415 | 0.260183 | 0.857785 | 85.881% |
| 1 | 0 | 157333.9 | 17.182% | 3.449279 | 63.974% | 0.096657 | 1.306472 | 0.309378 | 0.821468 | 80.309% |
| 2 | 0 | 171528.1 | 27.754% | 3.040750 | 68.241% | 0.077315 | 1.234562 | 0.338485 | 0.803399 | 77.492% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
