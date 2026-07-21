# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146863.9 | 0.000% | 8.119242 | 0.000% | 0.254027 | 2.727082 | 0.235778 | 0.877793 | 89.424% |
| 0.25 | 0 | 155672.5 | 5.998% | 6.796281 | 16.294% | 0.163078 | 2.439699 | 0.261891 | 0.874731 | 88.698% |
| 0.5 | 0 | 163793.2 | 11.527% | 5.125260 | 36.875% | 0.121392 | 1.679215 | 0.245572 | 0.850897 | 84.986% |
| 1 | 0 | 173985.3 | 18.467% | 3.534942 | 56.462% | 0.089357 | 1.211306 | 0.293680 | 0.820360 | 79.844% |
| 2 | 0 | 189274.6 | 28.878% | 2.884369 | 64.475% | 0.070164 | 0.929479 | 0.271847 | 0.798612 | 75.943% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
