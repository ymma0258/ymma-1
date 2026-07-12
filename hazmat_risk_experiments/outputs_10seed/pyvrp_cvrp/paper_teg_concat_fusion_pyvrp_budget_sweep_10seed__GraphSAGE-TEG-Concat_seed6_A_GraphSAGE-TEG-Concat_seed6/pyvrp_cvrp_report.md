# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.7 | 0.000% | 8.923025 | 0.000% | 0.289420 | 2.546310 | 0.150959 | 0.876615 | 89.642% |
| 0.25 | 0 | 145135.8 | 8.097% | 5.424387 | 39.209% | 0.160769 | 1.647817 | 0.215608 | 0.860078 | 86.349% |
| 0.5 | 0 | 152414.9 | 13.518% | 4.525487 | 49.283% | 0.113669 | 1.547868 | 0.265677 | 0.842419 | 83.903% |
| 1 | 0 | 162939.0 | 21.357% | 2.823595 | 68.356% | 0.059265 | 0.997919 | 0.298628 | 0.786569 | 74.964% |
| 2 | 0 | 178546.0 | 32.981% | 2.408605 | 73.007% | 0.049867 | 0.958642 | 0.305172 | 0.762065 | 70.911% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
