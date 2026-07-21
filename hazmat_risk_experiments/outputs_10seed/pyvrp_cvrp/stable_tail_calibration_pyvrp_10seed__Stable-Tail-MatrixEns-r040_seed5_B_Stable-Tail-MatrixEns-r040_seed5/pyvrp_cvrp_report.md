# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 4.673143 | 0.000% | 0.145571 | 1.551335 | 0.224228 | 0.874710 | 88.969% |
| 0.25 | 0 | 156220.4 | 6.371% | 3.945882 | 15.563% | 0.100361 | 1.298861 | 0.219023 | 0.872718 | 88.402% |
| 0.5 | 0 | 164393.8 | 11.936% | 3.084371 | 33.998% | 0.072900 | 0.919614 | 0.215212 | 0.851464 | 85.049% |
| 1 | 0 | 174703.2 | 18.956% | 2.065913 | 55.792% | 0.051252 | 0.711874 | 0.286454 | 0.815926 | 79.323% |
| 2 | 0 | 190202.4 | 29.509% | 1.670246 | 64.259% | 0.040513 | 0.546722 | 0.274957 | 0.791515 | 75.136% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
