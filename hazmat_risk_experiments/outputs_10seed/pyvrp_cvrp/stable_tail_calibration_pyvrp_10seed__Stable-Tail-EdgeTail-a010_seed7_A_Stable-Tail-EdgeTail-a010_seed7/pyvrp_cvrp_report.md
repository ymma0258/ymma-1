# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.6 | 0.000% | 9.318065 | 0.000% | 0.309971 | 2.628273 | 0.167890 | 0.872713 | 89.431% |
| 0.25 | 0 | 143373.2 | 6.625% | 5.530806 | 40.644% | 0.160455 | 1.930712 | 0.242196 | 0.851369 | 85.695% |
| 0.5 | 0 | 149317.8 | 11.046% | 4.545620 | 51.217% | 0.130210 | 1.646746 | 0.257635 | 0.834779 | 83.041% |
| 1 | 0 | 158812.5 | 18.107% | 3.360384 | 63.937% | 0.091830 | 1.371662 | 0.311916 | 0.803652 | 77.845% |
| 2 | 0 | 172163.4 | 28.036% | 2.573649 | 72.380% | 0.059993 | 0.842175 | 0.235973 | 0.758324 | 71.094% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
