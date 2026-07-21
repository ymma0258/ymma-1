# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.061821 | 0.000% | 0.205088 | 1.993881 | 0.147732 | 0.865569 | 88.558% |
| 0.25 | 0 | 143263.4 | 6.915% | 4.361403 | 38.240% | 0.123280 | 1.444861 | 0.260352 | 0.843121 | 84.777% |
| 0.5 | 0 | 149402.2 | 11.496% | 3.571960 | 49.419% | 0.103496 | 1.280832 | 0.301779 | 0.818466 | 81.501% |
| 1 | 0 | 158984.9 | 18.647% | 2.606787 | 63.086% | 0.069226 | 0.825130 | 0.255467 | 0.774837 | 75.525% |
| 2 | 0 | 173259.9 | 29.300% | 2.056289 | 70.882% | 0.047561 | 0.727202 | 0.292290 | 0.731317 | 69.447% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
