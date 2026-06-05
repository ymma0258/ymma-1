# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.4 | 0.000% | 8.026112 | 0.000% | 0.241512 | 2.589930 | 0.219252 | 0.840837 | 87.001% |
| 1 | 0 | 159904.8 | 19.334% | 3.207165 | 60.041% | 0.065190 | 1.148022 | 0.277382 | 0.713286 | 70.439% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
