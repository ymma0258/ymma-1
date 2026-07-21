# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.2 | 0.000% | 9.518359 | 0.000% | 0.307345 | 2.527135 | 0.146263 | 0.872624 | 89.716% |
| 0.25 | 0 | 142056.3 | 5.751% | 6.216597 | 34.688% | 0.190818 | 1.860917 | 0.198819 | 0.864050 | 87.525% |
| 0.5 | 0 | 148119.9 | 10.265% | 4.823083 | 49.329% | 0.125692 | 1.832811 | 0.279225 | 0.843118 | 84.262% |
| 1 | 0 | 156595.0 | 16.574% | 3.251731 | 65.837% | 0.071499 | 1.093767 | 0.239205 | 0.795869 | 77.206% |
| 2 | 0 | 169978.6 | 26.537% | 2.703344 | 71.599% | 0.058453 | 0.830831 | 0.204229 | 0.766931 | 72.593% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
