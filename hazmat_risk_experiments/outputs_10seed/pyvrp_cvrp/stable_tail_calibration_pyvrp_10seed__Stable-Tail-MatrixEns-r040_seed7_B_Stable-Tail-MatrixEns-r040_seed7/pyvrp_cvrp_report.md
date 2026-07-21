# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 6.123642 | 0.000% | 0.185063 | 1.853078 | 0.182390 | 0.878917 | 90.692% |
| 0.25 | 0 | 157440.7 | 7.202% | 4.921447 | 19.632% | 0.140094 | 1.510557 | 0.214823 | 0.876526 | 89.546% |
| 0.5 | 0 | 166926.6 | 13.661% | 3.367291 | 45.012% | 0.092265 | 1.247725 | 0.274241 | 0.854068 | 85.221% |
| 1 | 0 | 177974.7 | 21.183% | 2.384793 | 61.056% | 0.060640 | 0.811807 | 0.268034 | 0.827731 | 80.434% |
| 2 | 0 | 194472.6 | 32.417% | 2.084836 | 65.954% | 0.050266 | 0.640699 | 0.210232 | 0.813536 | 78.011% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
