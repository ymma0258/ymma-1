# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.786940 | 0.000% | 0.219918 | 2.386595 | 0.190584 | 0.845807 | 87.210% |
| 1 | 0 | 156724.7 | 16.961% | 3.065668 | 60.631% | 0.072187 | 0.853545 | 0.184027 | 0.716580 | 70.849% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
