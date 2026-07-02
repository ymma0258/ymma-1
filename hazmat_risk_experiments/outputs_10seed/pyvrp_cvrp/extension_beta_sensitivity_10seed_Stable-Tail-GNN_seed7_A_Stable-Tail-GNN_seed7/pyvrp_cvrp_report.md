# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 8.860071 | 0.000% | 0.280270 | 2.612395 | 0.153796 | 0.875752 | 89.901% |
| 0.5 | 0 | 149196.8 | 11.343% | 4.567495 | 48.449% | 0.116005 | 1.451106 | 0.184935 | 0.845583 | 84.080% |
| 1 | 0 | 158498.5 | 18.285% | 3.260477 | 63.200% | 0.072756 | 1.191802 | 0.291764 | 0.805873 | 77.756% |
| 1.5 | 0 | 164975.1 | 23.118% | 2.664768 | 69.924% | 0.051527 | 0.790649 | 0.237728 | 0.782349 | 73.604% |
| 2 | 0 | 170864.4 | 27.513% | 2.535759 | 71.380% | 0.048612 | 0.808732 | 0.260480 | 0.765709 | 71.399% |
| 3 | 0 | 182209.5 | 35.980% | 2.355461 | 73.415% | 0.046754 | 0.897270 | 0.301507 | 0.743651 | 68.383% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
