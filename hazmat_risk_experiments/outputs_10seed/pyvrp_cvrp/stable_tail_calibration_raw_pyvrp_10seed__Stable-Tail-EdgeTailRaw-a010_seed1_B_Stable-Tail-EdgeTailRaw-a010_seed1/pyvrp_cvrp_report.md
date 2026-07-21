# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.8 | 0.000% | 10.027275 | 0.000% | 0.318818 | 3.409350 | 0.255640 | 0.874632 | 90.180% |
| 0.25 | 0 | 156108.2 | 6.006% | 8.483214 | 15.399% | 0.253696 | 3.036119 | 0.259435 | 0.871401 | 89.216% |
| 0.5 | 0 | 164291.2 | 11.563% | 6.573661 | 34.442% | 0.175930 | 2.019663 | 0.222034 | 0.859555 | 86.660% |
| 1 | 0 | 174292.2 | 18.354% | 3.935042 | 60.757% | 0.096855 | 1.387411 | 0.248992 | 0.814572 | 79.189% |
| 2 | 0 | 187865.2 | 27.571% | 3.339764 | 66.693% | 0.069208 | 1.128228 | 0.243867 | 0.797445 | 76.088% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
