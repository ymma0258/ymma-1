# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 8.720420 | 0.000% | 0.264194 | 2.770401 | 0.203663 | 0.876027 | 89.446% |
| 0.25 | 0 | 155427.4 | 5.783% | 7.675797 | 11.979% | 0.218968 | 2.543853 | 0.223243 | 0.874086 | 88.877% |
| 0.5 | 0 | 163430.2 | 11.230% | 5.826644 | 33.184% | 0.157391 | 1.856272 | 0.239817 | 0.859701 | 85.904% |
| 1 | 0 | 173670.0 | 18.199% | 4.055565 | 53.493% | 0.105011 | 1.610791 | 0.300611 | 0.825658 | 80.688% |
| 2 | 0 | 189207.6 | 28.773% | 3.236077 | 62.891% | 0.067815 | 1.325298 | 0.321610 | 0.804450 | 77.183% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
