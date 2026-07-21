# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 8.698776 | 0.000% | 0.276819 | 2.412801 | 0.157628 | 0.871022 | 89.375% |
| 0.25 | 0 | 142053.8 | 5.854% | 6.112243 | 29.734% | 0.189735 | 1.814991 | 0.189914 | 0.862993 | 87.619% |
| 0.5 | 0 | 147888.9 | 10.202% | 4.488631 | 48.399% | 0.115585 | 1.569185 | 0.229476 | 0.841684 | 84.163% |
| 1 | 0 | 156546.8 | 16.653% | 3.157144 | 63.706% | 0.071065 | 0.995872 | 0.201736 | 0.799114 | 77.742% |
| 2 | 0 | 169578.2 | 26.364% | 2.643275 | 69.613% | 0.055287 | 0.789073 | 0.224909 | 0.776255 | 73.899% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
