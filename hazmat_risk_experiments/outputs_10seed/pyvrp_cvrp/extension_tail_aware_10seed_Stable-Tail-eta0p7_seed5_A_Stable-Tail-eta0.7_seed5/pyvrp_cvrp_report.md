# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.808221 | 0.000% | 0.204228 | 2.658346 | 0.177619 | 0.874866 | 88.881% |
| 1 | 0 | 156213.2 | 16.579% | 3.008485 | 65.845% | 0.059725 | 1.268050 | 0.330656 | 0.768439 | 72.604% |
| 2 | 0 | 167209.6 | 24.786% | 2.293484 | 73.962% | 0.039832 | 0.774718 | 0.257267 | 0.708123 | 64.436% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
