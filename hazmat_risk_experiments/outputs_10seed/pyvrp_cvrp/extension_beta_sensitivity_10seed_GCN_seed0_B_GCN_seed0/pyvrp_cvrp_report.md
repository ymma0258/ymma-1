# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 7.918001 | 0.000% | 0.244567 | 2.611301 | 0.231434 | 0.858147 | 88.643% |
| 0.5 | 0 | 166900.1 | 13.746% | 4.966745 | 37.273% | 0.124271 | 1.532225 | 0.217022 | 0.840281 | 85.062% |
| 1 | 0 | 179666.8 | 22.446% | 3.614334 | 54.353% | 0.089302 | 1.239985 | 0.287076 | 0.808708 | 80.269% |
| 1.5 | 0 | 188627.7 | 28.553% | 3.074066 | 61.176% | 0.073584 | 0.942518 | 0.233390 | 0.788397 | 77.108% |
| 2 | 0 | 196924.8 | 34.208% | 2.776209 | 64.938% | 0.061636 | 0.853356 | 0.246100 | 0.769836 | 74.278% |
| 3 | 0 | 212877.7 | 45.080% | 2.682740 | 66.118% | 0.058663 | 0.842998 | 0.264389 | 0.762170 | 73.223% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
