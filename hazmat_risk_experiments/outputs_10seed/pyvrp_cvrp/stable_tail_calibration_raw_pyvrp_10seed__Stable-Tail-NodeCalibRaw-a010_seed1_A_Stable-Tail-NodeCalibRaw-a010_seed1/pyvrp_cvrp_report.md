# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 9.324137 | 0.000% | 0.312434 | 2.826983 | 0.166756 | 0.874136 | 89.675% |
| 0.25 | 0 | 142153.7 | 5.876% | 6.799826 | 27.073% | 0.202618 | 2.032843 | 0.203148 | 0.864811 | 88.051% |
| 0.5 | 0 | 147945.6 | 10.189% | 4.871791 | 47.751% | 0.132316 | 1.709329 | 0.249136 | 0.842997 | 84.322% |
| 1 | 0 | 156448.0 | 16.522% | 3.170072 | 66.001% | 0.069241 | 1.108628 | 0.265047 | 0.792509 | 76.637% |
| 2 | 0 | 169149.0 | 25.982% | 2.863435 | 69.290% | 0.061860 | 0.941704 | 0.248037 | 0.782281 | 74.849% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
