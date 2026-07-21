# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 7.226437 | 0.000% | 0.222748 | 2.242169 | 0.190266 | 0.859921 | 87.730% |
| 0.25 | 0 | 156317.8 | 6.437% | 5.840445 | 19.179% | 0.136504 | 1.878752 | 0.209754 | 0.853694 | 86.648% |
| 0.5 | 0 | 164801.8 | 12.214% | 4.470216 | 38.141% | 0.110142 | 1.449048 | 0.229230 | 0.834890 | 83.264% |
| 1 | 0 | 175628.7 | 19.586% | 2.874859 | 60.217% | 0.066518 | 0.964572 | 0.205625 | 0.781539 | 75.437% |
| 2 | 0 | 190296.1 | 29.573% | 2.329926 | 67.758% | 0.050460 | 0.660503 | 0.191846 | 0.750368 | 70.328% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
