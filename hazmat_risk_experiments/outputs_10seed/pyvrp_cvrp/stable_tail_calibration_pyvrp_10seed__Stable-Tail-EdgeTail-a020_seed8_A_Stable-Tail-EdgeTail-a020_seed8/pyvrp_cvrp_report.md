# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.930221 | 0.000% | 0.243480 | 2.275236 | 0.166941 | 0.870916 | 88.990% |
| 0.25 | 0 | 142544.2 | 6.325% | 5.307912 | 33.067% | 0.149989 | 1.702502 | 0.233745 | 0.856906 | 86.682% |
| 0.5 | 0 | 148811.3 | 11.000% | 3.814678 | 51.897% | 0.102788 | 1.362707 | 0.243874 | 0.821181 | 81.573% |
| 1 | 0 | 157446.2 | 17.441% | 2.854703 | 64.002% | 0.071974 | 0.818291 | 0.186087 | 0.784698 | 76.028% |
| 2 | 0 | 171448.7 | 27.885% | 2.255967 | 71.552% | 0.045015 | 0.734943 | 0.239589 | 0.750142 | 70.519% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
