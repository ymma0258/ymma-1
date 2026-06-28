# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.442787 | 0.000% | 0.293933 | 3.399195 | 0.220726 | 0.856399 | 89.822% |
| 0.5 | 0 | 167615.8 | 14.233% | 7.450079 | 28.658% | 0.201941 | 2.301476 | 0.199687 | 0.850271 | 87.504% |
| 1 | 0 | 180891.4 | 23.281% | 5.343059 | 48.835% | 0.150212 | 1.700914 | 0.226783 | 0.819760 | 83.013% |
| 1.5 | 0 | 193151.8 | 31.637% | 4.687252 | 55.115% | 0.121526 | 1.943432 | 0.339200 | 0.803378 | 80.414% |
| 2 | 0 | 202983.1 | 38.337% | 4.059695 | 61.124% | 0.096341 | 1.398538 | 0.325219 | 0.785616 | 77.241% |
| 3 | 0 | 221403.2 | 50.891% | 3.948428 | 62.190% | 0.090642 | 1.394187 | 0.325501 | 0.781889 | 76.611% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
