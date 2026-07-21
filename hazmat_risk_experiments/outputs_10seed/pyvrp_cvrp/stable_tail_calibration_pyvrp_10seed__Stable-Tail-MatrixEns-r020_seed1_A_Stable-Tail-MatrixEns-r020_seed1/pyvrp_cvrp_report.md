# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 7.386178 | 0.000% | 0.235826 | 2.037952 | 0.146905 | 0.873385 | 89.825% |
| 0.25 | 0 | 141975.2 | 5.953% | 5.185259 | 29.798% | 0.155869 | 1.622575 | 0.205379 | 0.866110 | 87.941% |
| 0.5 | 0 | 147739.7 | 10.255% | 3.686983 | 50.083% | 0.090730 | 1.366050 | 0.243910 | 0.836981 | 83.464% |
| 1 | 0 | 156259.4 | 16.613% | 2.617157 | 64.567% | 0.056783 | 0.812985 | 0.186587 | 0.794137 | 77.091% |
| 2 | 0 | 168908.6 | 26.053% | 2.128054 | 71.189% | 0.041733 | 0.670036 | 0.230260 | 0.769027 | 72.810% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
