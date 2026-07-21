# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147396.9 | 0.000% | 8.847783 | 0.000% | 0.269424 | 2.897393 | 0.224273 | 0.875617 | 89.537% |
| 0.25 | 0 | 156249.8 | 6.006% | 7.370966 | 16.691% | 0.209755 | 2.437422 | 0.224223 | 0.872201 | 88.417% |
| 0.5 | 0 | 164468.1 | 11.582% | 5.980674 | 32.405% | 0.156355 | 1.877197 | 0.229324 | 0.859650 | 86.095% |
| 1 | 0 | 175191.3 | 18.857% | 3.979303 | 55.025% | 0.100269 | 1.478966 | 0.301179 | 0.823924 | 80.483% |
| 2 | 0 | 190888.5 | 29.506% | 3.342033 | 62.227% | 0.070391 | 1.366755 | 0.305892 | 0.804212 | 77.438% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
