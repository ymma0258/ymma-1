# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 9.300626 | 0.000% | 0.297959 | 2.480795 | 0.139946 | 0.874001 | 89.992% |
| 0.25 | 0 | 141732.0 | 5.719% | 6.688719 | 28.083% | 0.205497 | 2.053288 | 0.217857 | 0.870612 | 88.634% |
| 0.5 | 0 | 147490.9 | 10.015% | 4.590235 | 50.646% | 0.118403 | 1.501911 | 0.201220 | 0.840960 | 83.729% |
| 1 | 0 | 155790.6 | 16.206% | 3.206955 | 65.519% | 0.069100 | 1.051181 | 0.232378 | 0.789719 | 76.591% |
| 2 | 0 | 168333.6 | 25.562% | 2.840254 | 69.462% | 0.056536 | 0.823169 | 0.208268 | 0.779419 | 74.460% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
