# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.047752 | 0.000% | 0.234412 | 2.263909 | 0.146414 | 0.867043 | 88.834% |
| 0.25 | 0 | 142630.2 | 6.442% | 5.834347 | 27.503% | 0.169619 | 1.786654 | 0.227438 | 0.857236 | 86.990% |
| 0.5 | 0 | 148494.7 | 10.819% | 4.152450 | 48.402% | 0.122220 | 1.544418 | 0.306162 | 0.823272 | 82.341% |
| 1 | 0 | 157503.5 | 17.542% | 2.841656 | 64.690% | 0.075504 | 0.895201 | 0.264388 | 0.777172 | 75.723% |
| 2 | 0 | 171326.1 | 27.857% | 2.297227 | 71.455% | 0.053845 | 0.856104 | 0.306597 | 0.734221 | 69.783% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
