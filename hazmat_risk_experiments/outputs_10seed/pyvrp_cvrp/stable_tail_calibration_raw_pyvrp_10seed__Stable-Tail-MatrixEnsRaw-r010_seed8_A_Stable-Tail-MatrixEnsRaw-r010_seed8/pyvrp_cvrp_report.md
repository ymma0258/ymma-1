# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.7 | 0.000% | 6.932235 | 0.000% | 0.214590 | 2.012831 | 0.166918 | 0.868774 | 88.671% |
| 0.25 | 0 | 142932.5 | 6.615% | 5.205567 | 24.908% | 0.147984 | 1.656530 | 0.235833 | 0.862782 | 87.613% |
| 0.5 | 0 | 149574.2 | 11.569% | 3.711631 | 46.458% | 0.109502 | 1.311445 | 0.251653 | 0.833924 | 83.063% |
| 1 | 0 | 158411.4 | 18.160% | 2.450697 | 64.648% | 0.061901 | 0.789275 | 0.237271 | 0.777535 | 75.069% |
| 2 | 0 | 173123.4 | 29.134% | 2.086497 | 69.902% | 0.043198 | 0.625558 | 0.212353 | 0.754079 | 71.280% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
