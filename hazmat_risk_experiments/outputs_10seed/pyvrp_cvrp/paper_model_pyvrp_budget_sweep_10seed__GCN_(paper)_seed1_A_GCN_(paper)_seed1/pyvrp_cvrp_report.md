# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.9 | 0.000% | 8.028260 | 0.000% | 0.248190 | 2.378280 | 0.172059 | 0.870404 | 89.125% |
| 0.25 | 0 | 142495.8 | 6.289% | 5.493026 | 31.579% | 0.150187 | 1.586021 | 0.183865 | 0.855291 | 86.659% |
| 0.5 | 0 | 148387.4 | 10.683% | 4.377887 | 45.469% | 0.124558 | 1.733399 | 0.298083 | 0.835482 | 83.833% |
| 1 | 0 | 157005.8 | 17.112% | 2.990054 | 62.756% | 0.080011 | 1.042167 | 0.259160 | 0.783632 | 76.426% |
| 2 | 0 | 170223.4 | 26.971% | 2.227466 | 72.255% | 0.044956 | 0.777729 | 0.266164 | 0.731117 | 68.505% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
