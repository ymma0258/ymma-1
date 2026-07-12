# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146930.6 | 0.000% | 8.775557 | 0.000% | 0.258753 | 3.172609 | 0.288469 | 0.883452 | 89.770% |
| 0.25 | 0 | 158131.1 | 7.623% | 7.741124 | 11.788% | 0.226730 | 2.833392 | 0.303833 | 0.883327 | 89.612% |
| 0.5 | 0 | 167871.8 | 14.252% | 5.432196 | 38.099% | 0.145956 | 1.824647 | 0.250185 | 0.864380 | 85.807% |
| 1 | 0 | 181016.2 | 23.198% | 3.982616 | 54.617% | 0.103856 | 1.577702 | 0.324875 | 0.852301 | 82.502% |
| 2 | 0 | 201168.3 | 36.914% | 3.276397 | 62.665% | 0.077570 | 1.602975 | 0.396304 | 0.830310 | 78.453% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
