# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.035681 | 0.000% | 0.219598 | 2.415906 | 0.234400 | 0.876974 | 89.513% |
| 0.25 | 0 | 155941.8 | 6.277% | 6.114517 | 13.093% | 0.148485 | 1.933654 | 0.209953 | 0.873246 | 88.847% |
| 0.5 | 0 | 164633.3 | 12.201% | 4.047767 | 42.468% | 0.094576 | 1.300305 | 0.227583 | 0.837749 | 83.076% |
| 1 | 0 | 174255.2 | 18.758% | 2.892914 | 58.882% | 0.068165 | 1.181970 | 0.354783 | 0.811699 | 78.206% |
| 2 | 0 | 190068.2 | 29.535% | 2.356421 | 66.508% | 0.054672 | 0.877631 | 0.314712 | 0.782064 | 73.425% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
