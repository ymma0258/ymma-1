# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147396.9 | 0.000% | 8.941449 | 0.000% | 0.279635 | 3.478450 | 0.319771 | 0.873978 | 89.549% |
| 0.25 | 0 | 156663.1 | 6.287% | 7.519605 | 15.902% | 0.227161 | 2.635451 | 0.294274 | 0.871581 | 88.826% |
| 0.5 | 0 | 165531.8 | 12.303% | 6.004927 | 32.842% | 0.160370 | 2.195466 | 0.250186 | 0.858998 | 86.575% |
| 1 | 0 | 177999.1 | 20.762% | 4.351844 | 51.330% | 0.117116 | 1.825689 | 0.329966 | 0.845035 | 83.230% |
| 2 | 0 | 196978.4 | 33.638% | 3.466606 | 61.230% | 0.085317 | 1.679361 | 0.389825 | 0.819605 | 78.884% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
