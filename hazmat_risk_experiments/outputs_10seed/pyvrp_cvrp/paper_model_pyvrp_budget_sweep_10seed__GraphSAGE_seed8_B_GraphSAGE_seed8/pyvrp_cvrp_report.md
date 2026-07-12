# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.3 | 0.000% | 8.061943 | 0.000% | 0.244460 | 2.589855 | 0.208547 | 0.865484 | 88.916% |
| 0.25 | 0 | 157230.9 | 6.671% | 6.911968 | 14.264% | 0.175084 | 2.059714 | 0.171637 | 0.865250 | 88.148% |
| 0.5 | 0 | 166047.4 | 12.653% | 5.486726 | 31.943% | 0.133896 | 1.816326 | 0.233012 | 0.845157 | 85.273% |
| 1 | 0 | 176495.6 | 19.741% | 3.226020 | 59.985% | 0.076010 | 1.100050 | 0.277342 | 0.792525 | 76.638% |
| 2 | 0 | 192003.1 | 30.262% | 2.632775 | 67.343% | 0.057281 | 0.899271 | 0.264169 | 0.760647 | 71.591% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
