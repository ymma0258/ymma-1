# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.6 | 0.000% | 9.149314 | 0.000% | 0.292448 | 2.576132 | 0.164530 | 0.877019 | 90.013% |
| 0.25 | 0 | 143462.6 | 6.692% | 6.639130 | 27.436% | 0.205668 | 1.954284 | 0.194158 | 0.871449 | 88.701% |
| 0.5 | 0 | 150339.9 | 11.806% | 4.925478 | 46.166% | 0.148285 | 1.692830 | 0.296898 | 0.853300 | 85.534% |
| 1 | 0 | 159726.2 | 18.787% | 3.440214 | 62.399% | 0.085439 | 1.185852 | 0.302874 | 0.814960 | 79.757% |
| 2 | 0 | 174681.0 | 29.909% | 2.793998 | 69.462% | 0.065874 | 1.051806 | 0.349932 | 0.787299 | 75.489% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
