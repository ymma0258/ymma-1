# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.7 | 0.000% | 8.353141 | 0.000% | 0.264745 | 2.637590 | 0.209995 | 0.872513 | 89.589% |
| 0.25 | 0 | 143485.5 | 6.974% | 5.323179 | 36.273% | 0.149786 | 1.824133 | 0.257485 | 0.849524 | 86.349% |
| 0.5 | 0 | 149749.2 | 11.643% | 4.255954 | 49.050% | 0.105232 | 1.671356 | 0.272010 | 0.826664 | 83.255% |
| 1 | 0 | 158900.0 | 18.466% | 2.937014 | 64.839% | 0.066496 | 1.105272 | 0.278221 | 0.776527 | 76.168% |
| 2 | 0 | 173327.8 | 29.222% | 2.404552 | 71.214% | 0.051278 | 0.740510 | 0.214615 | 0.740749 | 70.974% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
