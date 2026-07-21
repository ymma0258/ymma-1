# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.0 | 0.000% | 7.746248 | 0.000% | 0.243203 | 2.517510 | 0.229903 | 0.873523 | 89.136% |
| 0.25 | 0 | 156767.7 | 6.357% | 6.422714 | 17.086% | 0.152657 | 2.234596 | 0.268350 | 0.868484 | 87.849% |
| 0.5 | 0 | 165671.8 | 12.398% | 5.386496 | 30.463% | 0.133322 | 1.788782 | 0.239738 | 0.856199 | 85.798% |
| 1 | 0 | 176145.9 | 19.504% | 3.479364 | 55.083% | 0.087572 | 1.294829 | 0.305359 | 0.816423 | 79.398% |
| 2 | 0 | 192241.7 | 30.424% | 2.769187 | 64.251% | 0.065774 | 0.871782 | 0.277299 | 0.787269 | 74.446% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
