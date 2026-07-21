# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.148763 | 0.000% | 0.237695 | 2.294545 | 0.146461 | 0.867814 | 88.966% |
| 0.25 | 0 | 142467.9 | 6.321% | 5.664754 | 30.483% | 0.165037 | 1.843682 | 0.264890 | 0.854443 | 86.665% |
| 0.5 | 0 | 148165.8 | 10.573% | 4.173241 | 48.787% | 0.123310 | 1.510749 | 0.300359 | 0.823267 | 82.301% |
| 1 | 0 | 156946.9 | 17.126% | 2.924354 | 64.113% | 0.078191 | 0.943263 | 0.247568 | 0.779168 | 75.992% |
| 2 | 0 | 170398.2 | 27.165% | 2.281033 | 72.008% | 0.052991 | 0.836425 | 0.293535 | 0.726691 | 68.869% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
