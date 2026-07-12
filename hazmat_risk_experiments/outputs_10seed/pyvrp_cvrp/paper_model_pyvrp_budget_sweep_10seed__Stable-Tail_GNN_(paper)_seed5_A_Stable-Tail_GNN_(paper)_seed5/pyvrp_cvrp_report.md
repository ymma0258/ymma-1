# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134131.6 | 0.000% | 7.154770 | 0.000% | 0.220178 | 2.082018 | 0.182356 | 0.873642 | 88.886% |
| 0.25 | 0 | 142715.6 | 6.400% | 5.114765 | 28.513% | 0.144688 | 1.745690 | 0.235358 | 0.859305 | 86.482% |
| 0.5 | 0 | 148406.9 | 10.643% | 3.640050 | 49.124% | 0.105649 | 1.390081 | 0.298847 | 0.824510 | 81.343% |
| 1 | 0 | 156522.2 | 16.693% | 2.530445 | 64.633% | 0.065274 | 0.937322 | 0.267795 | 0.770166 | 73.660% |
| 2 | 0 | 168029.1 | 25.272% | 1.845178 | 74.211% | 0.039197 | 0.605669 | 0.242176 | 0.710535 | 64.729% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
