# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.786940 | 0.000% | 0.219918 | 2.386595 | 0.190584 | 0.845807 | 87.210% |
| 1 | 0 | 156728.0 | 16.963% | 3.025073 | 61.152% | 0.069048 | 0.853545 | 0.189990 | 0.712402 | 70.389% |
| 1 | 1 | 165299.2 | 23.360% | 2.145632 | 72.446% | 0.035071 | 0.587488 | 0.159587 | 0.606442 | 57.248% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
