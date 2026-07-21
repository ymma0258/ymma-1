# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.4 | 0.000% | 8.056534 | 0.000% | 0.252666 | 2.395645 | 0.189936 | 0.883121 | 90.304% |
| 0.25 | 0 | 142509.8 | 6.088% | 4.914784 | 38.996% | 0.146218 | 1.611835 | 0.219830 | 0.864999 | 86.946% |
| 0.5 | 0 | 148356.4 | 10.441% | 3.576389 | 55.609% | 0.100752 | 1.330251 | 0.280899 | 0.829508 | 82.036% |
| 1 | 0 | 156175.7 | 16.261% | 2.401610 | 70.191% | 0.052697 | 0.992583 | 0.302203 | 0.778873 | 74.340% |
| 2 | 0 | 168378.2 | 25.345% | 1.750178 | 78.276% | 0.033603 | 0.555436 | 0.226921 | 0.722219 | 65.427% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
