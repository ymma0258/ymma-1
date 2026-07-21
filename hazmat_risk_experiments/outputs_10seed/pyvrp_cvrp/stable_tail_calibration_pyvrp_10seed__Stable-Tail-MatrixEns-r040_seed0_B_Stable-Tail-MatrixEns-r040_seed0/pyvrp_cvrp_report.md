# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 4.541379 | 0.000% | 0.124255 | 1.546679 | 0.252488 | 0.878659 | 89.508% |
| 0.25 | 0 | 156354.4 | 6.462% | 3.915795 | 13.775% | 0.095230 | 1.327854 | 0.256987 | 0.872914 | 88.579% |
| 0.5 | 0 | 164553.7 | 12.045% | 2.780522 | 38.774% | 0.070823 | 0.938380 | 0.223508 | 0.850830 | 84.533% |
| 1 | 0 | 174867.6 | 19.068% | 1.886357 | 58.463% | 0.048015 | 0.702160 | 0.286098 | 0.813157 | 78.528% |
| 2 | 0 | 189712.2 | 29.176% | 1.458878 | 67.876% | 0.029403 | 0.511706 | 0.249771 | 0.777990 | 72.527% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
