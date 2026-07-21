# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134597.6 | 0.000% | 7.802734 | 0.000% | 0.249224 | 2.186403 | 0.149045 | 0.874161 | 88.852% |
| 0.25 | 0 | 142376.3 | 5.779% | 5.348266 | 31.457% | 0.148804 | 1.697840 | 0.198930 | 0.861619 | 86.972% |
| 0.5 | 0 | 147920.0 | 9.898% | 3.738196 | 52.091% | 0.110260 | 1.563791 | 0.345718 | 0.830495 | 82.170% |
| 1 | 0 | 155996.3 | 15.898% | 2.516540 | 67.748% | 0.064745 | 0.976550 | 0.268867 | 0.772806 | 73.842% |
| 2 | 0 | 167203.4 | 24.225% | 1.995322 | 74.428% | 0.044961 | 0.646617 | 0.239683 | 0.729644 | 67.484% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
