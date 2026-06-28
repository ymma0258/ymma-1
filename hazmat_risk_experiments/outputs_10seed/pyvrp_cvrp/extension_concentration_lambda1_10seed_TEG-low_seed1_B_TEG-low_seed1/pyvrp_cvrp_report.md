# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 8.339548 | 0.000% | 0.242076 | 2.653866 | 0.207785 | 0.836548 | 86.597% |
| 1 | 0 | 176146.6 | 20.047% | 3.952516 | 52.605% | 0.078076 | 1.166958 | 0.191460 | 0.737529 | 73.876% |
| 1 | 1 | 189703.5 | 29.287% | 3.092520 | 62.917% | 0.057968 | 1.070690 | 0.257129 | 0.684760 | 66.949% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
