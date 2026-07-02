# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.280496 | 0.000% | 0.208685 | 2.332222 | 0.202410 | 0.859043 | 88.408% |
| 0.5 | 0 | 148900.3 | 11.122% | 4.154927 | 42.931% | 0.115960 | 1.539657 | 0.265273 | 0.823973 | 83.222% |
| 1 | 0 | 157217.6 | 17.329% | 2.677873 | 63.219% | 0.063408 | 0.917234 | 0.228815 | 0.753572 | 73.928% |
| 1.5 | 0 | 163921.2 | 22.331% | 2.582575 | 64.527% | 0.058297 | 0.829821 | 0.236497 | 0.748194 | 73.076% |
| 2 | 0 | 169843.4 | 26.751% | 2.205249 | 69.710% | 0.041354 | 0.706653 | 0.243928 | 0.706663 | 67.507% |
| 3 | 0 | 179714.4 | 34.118% | 1.822260 | 74.971% | 0.028329 | 0.599971 | 0.236489 | 0.657740 | 61.146% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
