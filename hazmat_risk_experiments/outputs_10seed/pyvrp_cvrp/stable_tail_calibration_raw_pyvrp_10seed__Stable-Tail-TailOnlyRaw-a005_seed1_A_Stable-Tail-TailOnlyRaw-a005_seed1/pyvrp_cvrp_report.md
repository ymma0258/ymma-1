# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 9.431085 | 0.000% | 0.305092 | 2.528865 | 0.139924 | 0.869833 | 89.177% |
| 0.25 | 0 | 142106.7 | 5.788% | 6.364116 | 32.520% | 0.192542 | 2.024412 | 0.200823 | 0.861034 | 87.467% |
| 0.5 | 0 | 147922.2 | 10.117% | 4.850025 | 48.574% | 0.126791 | 1.561667 | 0.204772 | 0.844289 | 84.394% |
| 1 | 0 | 156526.7 | 16.523% | 3.319901 | 64.798% | 0.076949 | 1.131681 | 0.242203 | 0.796354 | 77.344% |
| 2 | 0 | 169330.6 | 26.054% | 2.785252 | 70.467% | 0.057031 | 0.896033 | 0.250349 | 0.773222 | 73.544% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
