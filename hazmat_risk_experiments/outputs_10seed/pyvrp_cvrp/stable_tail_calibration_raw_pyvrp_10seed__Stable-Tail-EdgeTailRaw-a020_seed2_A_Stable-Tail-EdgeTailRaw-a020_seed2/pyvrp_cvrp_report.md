# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 9.348958 | 0.000% | 0.310931 | 2.903369 | 0.192937 | 0.878230 | 89.552% |
| 0.25 | 0 | 142408.6 | 6.013% | 5.877141 | 37.136% | 0.170394 | 2.158414 | 0.269894 | 0.865764 | 87.676% |
| 0.5 | 0 | 148501.8 | 10.549% | 4.930378 | 47.263% | 0.145169 | 1.849404 | 0.286701 | 0.857494 | 85.901% |
| 1 | 0 | 157321.8 | 17.115% | 3.432160 | 63.288% | 0.094348 | 1.291023 | 0.299424 | 0.819334 | 80.155% |
| 2 | 0 | 171740.2 | 27.848% | 2.968345 | 68.249% | 0.072354 | 1.280922 | 0.350617 | 0.800717 | 77.060% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
