# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.3 | 0.000% | 9.505018 | 0.000% | 0.313648 | 2.820399 | 0.180630 | 0.874877 | 89.456% |
| 0.25 | 0 | 143231.8 | 6.731% | 6.050986 | 36.339% | 0.180225 | 2.156902 | 0.252431 | 0.860879 | 87.048% |
| 0.5 | 0 | 149226.5 | 11.199% | 4.754767 | 49.976% | 0.139454 | 1.572264 | 0.213670 | 0.841291 | 83.931% |
| 1 | 0 | 158488.3 | 18.100% | 3.333711 | 64.927% | 0.091744 | 1.245808 | 0.289408 | 0.806221 | 78.139% |
| 2 | 0 | 171769.3 | 27.997% | 2.665975 | 71.952% | 0.060823 | 0.892212 | 0.255284 | 0.771433 | 72.802% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
