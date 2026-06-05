# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 133997.2 | 0.000% | 8.385621 | 0.000% | 0.261364 | 2.733652 | 0.212478 | 0.845622 | 87.542% |
| 0.25 | 143599.0 | 7.166% | 6.287080 | 25.025% | 0.182190 | 1.949577 | 0.225275 | 0.828747 | 84.748% |
| 0.5 | 150017.4 | 11.956% | 4.708079 | 43.855% | 0.134334 | 2.286402 | 0.384697 | 0.788385 | 79.960% |
| 1 | 159904.8 | 19.334% | 3.207165 | 61.754% | 0.065190 | 1.148022 | 0.277382 | 0.713286 | 70.439% |
| 2 | 173811.8 | 29.713% | 2.428375 | 71.041% | 0.040133 | 0.815643 | 0.224200 | 0.628806 | 60.366% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
