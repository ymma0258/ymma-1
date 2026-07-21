# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147130.6 | 0.000% | 9.708954 | 0.000% | 0.307804 | 3.300313 | 0.252707 | 0.872922 | 89.910% |
| 0.25 | 0 | 156339.6 | 6.259% | 7.755547 | 20.120% | 0.217671 | 2.586997 | 0.235410 | 0.867647 | 88.402% |
| 0.5 | 0 | 164609.2 | 11.880% | 6.536991 | 32.670% | 0.177497 | 2.261058 | 0.238523 | 0.860300 | 86.846% |
| 1 | 0 | 174470.3 | 18.582% | 4.073654 | 58.042% | 0.091544 | 1.378168 | 0.244809 | 0.819620 | 80.071% |
| 2 | 0 | 188545.9 | 28.149% | 3.376991 | 65.218% | 0.072814 | 1.168637 | 0.244931 | 0.797357 | 76.153% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
