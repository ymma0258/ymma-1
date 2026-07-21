# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 9.332451 | 0.000% | 0.285144 | 3.417202 | 0.280010 | 0.863375 | 89.494% |
| 0.25 | 0 | 156886.7 | 6.776% | 7.850112 | 15.884% | 0.217331 | 2.649870 | 0.274342 | 0.861313 | 88.587% |
| 0.5 | 0 | 166047.9 | 13.011% | 7.007517 | 24.912% | 0.181859 | 2.500316 | 0.268501 | 0.854372 | 87.381% |
| 1 | 0 | 178816.6 | 21.701% | 4.728405 | 49.334% | 0.125646 | 1.861604 | 0.316377 | 0.831961 | 82.921% |
| 2 | 0 | 198097.2 | 34.824% | 3.712199 | 60.223% | 0.082083 | 1.643829 | 0.364504 | 0.797829 | 77.694% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
