# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147330.9 | 0.000% | 8.677659 | 0.000% | 0.245397 | 2.629364 | 0.199616 | 0.873785 | 88.252% |
| 0.25 | 0 | 158271.8 | 7.426% | 7.027284 | 19.019% | 0.194008 | 2.177386 | 0.230275 | 0.862036 | 86.341% |
| 0.5 | 0 | 166992.6 | 13.345% | 5.219553 | 39.851% | 0.137160 | 1.800472 | 0.244810 | 0.834664 | 81.976% |
| 1 | 0 | 177241.6 | 20.302% | 3.544392 | 59.155% | 0.083473 | 1.343231 | 0.250008 | 0.789986 | 75.068% |
| 2 | 0 | 197104.1 | 33.783% | 3.325670 | 61.675% | 0.075254 | 1.503055 | 0.343249 | 0.787843 | 74.123% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
