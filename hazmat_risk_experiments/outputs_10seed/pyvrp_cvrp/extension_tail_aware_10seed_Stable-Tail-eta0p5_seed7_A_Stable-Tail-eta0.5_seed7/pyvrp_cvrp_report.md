# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 11.505187 | 0.000% | 0.223645 | 3.290236 | 0.147555 | 0.873956 | 89.737% |
| 1 | 0 | 158709.6 | 18.442% | 4.186675 | 63.611% | 0.060335 | 1.646071 | 0.341786 | 0.805207 | 77.201% |
| 2 | 0 | 171184.9 | 27.752% | 3.172802 | 72.423% | 0.041031 | 1.147890 | 0.302788 | 0.755018 | 69.768% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
