# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 6.250051 | 0.000% | 0.185513 | 1.944553 | 0.211122 | 0.884154 | 90.420% |
| 0.25 | 0 | 142403.9 | 6.273% | 3.587959 | 42.593% | 0.108132 | 1.220176 | 0.241751 | 0.859316 | 86.058% |
| 0.5 | 0 | 148089.0 | 10.516% | 3.019614 | 51.687% | 0.089825 | 1.222942 | 0.303038 | 0.840729 | 83.685% |
| 1 | 0 | 155785.2 | 16.259% | 1.900989 | 69.584% | 0.042818 | 0.798402 | 0.321246 | 0.777756 | 74.226% |
| 2 | 0 | 167869.2 | 25.277% | 1.420845 | 77.267% | 0.026032 | 0.497018 | 0.270444 | 0.731707 | 67.011% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
