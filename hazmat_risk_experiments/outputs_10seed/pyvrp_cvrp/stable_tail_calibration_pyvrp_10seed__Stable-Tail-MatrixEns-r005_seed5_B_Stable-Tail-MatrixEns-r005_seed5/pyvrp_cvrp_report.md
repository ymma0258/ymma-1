# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 7.275029 | 0.000% | 0.226183 | 2.394420 | 0.218898 | 0.873211 | 88.782% |
| 0.25 | 0 | 156267.0 | 6.354% | 6.278990 | 13.691% | 0.163240 | 2.064648 | 0.235790 | 0.870443 | 88.295% |
| 0.5 | 0 | 164354.6 | 11.859% | 4.421043 | 39.230% | 0.104496 | 1.324983 | 0.210089 | 0.838356 | 83.607% |
| 1 | 0 | 175469.1 | 19.423% | 3.254863 | 55.260% | 0.079614 | 1.141639 | 0.282695 | 0.814672 | 79.130% |
| 2 | 0 | 191262.9 | 30.172% | 2.643815 | 63.659% | 0.064379 | 0.906343 | 0.288484 | 0.792189 | 75.252% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
