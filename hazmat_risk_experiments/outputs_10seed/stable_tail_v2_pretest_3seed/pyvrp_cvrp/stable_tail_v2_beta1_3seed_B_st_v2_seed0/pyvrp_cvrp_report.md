# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 7.227117 | 0.000% | 0.215713 | 2.817890 | 0.304998 | 0.881497 | 89.783% |
| 1 | 0 | 174638.7 | 19.435% | 2.865035 | 60.357% | 0.070858 | 1.020150 | 0.276316 | 0.806541 | 77.380% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
