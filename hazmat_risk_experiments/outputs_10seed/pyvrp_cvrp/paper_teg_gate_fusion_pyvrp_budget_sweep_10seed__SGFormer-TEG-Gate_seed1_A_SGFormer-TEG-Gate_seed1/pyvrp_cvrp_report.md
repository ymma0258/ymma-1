# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 8.727990 | 0.000% | 0.279339 | 2.433721 | 0.158270 | 0.867315 | 88.679% |
| 0.25 | 0 | 141877.3 | 5.828% | 6.256477 | 28.317% | 0.172863 | 1.996443 | 0.212074 | 0.857456 | 86.502% |
| 0.5 | 0 | 147368.4 | 9.923% | 4.055951 | 53.529% | 0.112945 | 1.406804 | 0.244256 | 0.817998 | 80.186% |
| 1 | 0 | 155293.5 | 15.835% | 2.954906 | 66.144% | 0.066124 | 0.980587 | 0.232856 | 0.759735 | 72.475% |
| 2 | 0 | 166582.3 | 24.255% | 2.228828 | 74.463% | 0.042705 | 0.667476 | 0.182383 | 0.709575 | 64.914% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
