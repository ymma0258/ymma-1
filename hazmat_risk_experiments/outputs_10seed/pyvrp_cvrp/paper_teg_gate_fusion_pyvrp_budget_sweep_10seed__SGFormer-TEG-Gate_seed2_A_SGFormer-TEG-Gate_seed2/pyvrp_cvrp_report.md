# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.8 | 0.000% | 9.377770 | 0.000% | 0.314136 | 2.682617 | 0.165860 | 0.877404 | 90.020% |
| 0.25 | 0 | 142793.1 | 6.511% | 6.125066 | 34.685% | 0.158385 | 2.022090 | 0.266207 | 0.871581 | 87.481% |
| 0.5 | 0 | 149365.1 | 11.413% | 4.833781 | 48.455% | 0.128616 | 1.762943 | 0.273258 | 0.855915 | 84.447% |
| 1 | 0 | 158652.2 | 18.340% | 3.300468 | 64.805% | 0.085989 | 1.197968 | 0.302455 | 0.817619 | 78.036% |
| 2 | 0 | 174026.7 | 29.808% | 3.244150 | 65.406% | 0.084814 | 1.177087 | 0.287812 | 0.815360 | 77.709% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
