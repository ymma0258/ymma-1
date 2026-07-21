# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.0 | 0.000% | 9.524991 | 0.000% | 0.306938 | 2.645472 | 0.156697 | 0.876591 | 90.261% |
| 0.25 | 0 | 142121.3 | 5.904% | 6.118009 | 35.769% | 0.182336 | 1.805924 | 0.185926 | 0.860914 | 87.278% |
| 0.5 | 0 | 147961.6 | 10.256% | 4.726710 | 50.376% | 0.113880 | 1.471136 | 0.216344 | 0.846109 | 84.202% |
| 1 | 0 | 156523.6 | 16.636% | 3.196326 | 66.443% | 0.072840 | 1.176115 | 0.295375 | 0.792406 | 76.723% |
| 2 | 0 | 169214.4 | 26.093% | 2.613923 | 72.557% | 0.056540 | 0.834545 | 0.252875 | 0.762409 | 71.996% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
