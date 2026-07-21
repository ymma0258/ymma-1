# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.6 | 0.000% | 8.138625 | 0.000% | 0.262276 | 2.460767 | 0.189653 | 0.878408 | 89.517% |
| 0.25 | 0 | 142951.0 | 6.470% | 5.261612 | 35.350% | 0.149195 | 1.674917 | 0.218208 | 0.860559 | 86.550% |
| 0.5 | 0 | 148525.3 | 10.621% | 3.561685 | 56.237% | 0.102650 | 1.358667 | 0.314508 | 0.822318 | 80.769% |
| 1 | 0 | 156093.9 | 16.258% | 2.564171 | 68.494% | 0.066205 | 0.990610 | 0.283195 | 0.774706 | 74.182% |
| 2 | 0 | 167544.1 | 24.787% | 1.918397 | 76.428% | 0.041982 | 0.641412 | 0.230931 | 0.718603 | 66.018% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
