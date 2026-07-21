# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 6.512107 | 0.000% | 0.208084 | 1.800771 | 0.147870 | 0.874031 | 89.901% |
| 0.25 | 0 | 141909.7 | 5.904% | 4.429142 | 31.986% | 0.138132 | 1.312350 | 0.191255 | 0.863834 | 87.618% |
| 0.5 | 0 | 147735.1 | 10.252% | 3.247524 | 50.131% | 0.086491 | 1.092571 | 0.197078 | 0.840911 | 83.849% |
| 1 | 0 | 156041.6 | 16.451% | 2.255021 | 65.372% | 0.047592 | 0.745206 | 0.241089 | 0.791826 | 76.782% |
| 2 | 0 | 168658.5 | 25.866% | 1.729516 | 73.442% | 0.034526 | 0.535965 | 0.248046 | 0.754930 | 70.902% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
