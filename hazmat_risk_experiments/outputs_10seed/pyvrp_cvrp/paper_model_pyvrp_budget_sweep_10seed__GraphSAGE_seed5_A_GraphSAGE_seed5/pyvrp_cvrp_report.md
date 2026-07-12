# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134398.0 | 0.000% | 7.543812 | 0.000% | 0.229377 | 2.400462 | 0.188110 | 0.867929 | 88.348% |
| 0.25 | 0 | 142726.7 | 6.197% | 5.040261 | 33.187% | 0.135391 | 1.606638 | 0.231298 | 0.851350 | 85.639% |
| 0.5 | 0 | 149024.2 | 10.883% | 3.892149 | 48.406% | 0.105264 | 1.315672 | 0.253808 | 0.827287 | 81.965% |
| 1 | 0 | 157254.7 | 17.007% | 2.549747 | 66.201% | 0.064756 | 0.935313 | 0.294446 | 0.771766 | 73.616% |
| 2 | 0 | 170703.4 | 27.013% | 2.017241 | 73.260% | 0.035777 | 0.650820 | 0.248971 | 0.730900 | 67.309% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
