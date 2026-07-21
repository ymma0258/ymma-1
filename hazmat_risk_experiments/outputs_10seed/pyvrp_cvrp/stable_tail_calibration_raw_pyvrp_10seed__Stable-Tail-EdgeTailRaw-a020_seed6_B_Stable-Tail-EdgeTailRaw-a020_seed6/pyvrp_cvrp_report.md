# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.6 | 0.000% | 9.455409 | 0.000% | 0.295157 | 3.067842 | 0.221506 | 0.872524 | 89.601% |
| 0.25 | 0 | 158243.5 | 7.310% | 8.224895 | 13.014% | 0.217635 | 2.702759 | 0.242183 | 0.872195 | 89.527% |
| 0.5 | 0 | 168756.2 | 14.439% | 6.523106 | 31.012% | 0.166399 | 2.327873 | 0.272050 | 0.862769 | 87.353% |
| 1 | 0 | 182134.0 | 23.511% | 4.614433 | 51.198% | 0.113394 | 1.702717 | 0.334356 | 0.836082 | 82.663% |
| 2 | 0 | 202797.8 | 37.524% | 3.857369 | 59.205% | 0.099667 | 1.439620 | 0.342062 | 0.823155 | 79.934% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
