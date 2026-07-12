# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.948852 | 0.000% | 0.278597 | 2.662309 | 0.176754 | 0.884498 | 90.407% |
| 0.25 | 0 | 143773.0 | 7.295% | 5.830352 | 34.848% | 0.179151 | 1.920777 | 0.254596 | 0.876611 | 88.217% |
| 0.5 | 0 | 150664.3 | 12.438% | 4.696825 | 47.515% | 0.138190 | 1.781244 | 0.286493 | 0.862946 | 85.823% |
| 1 | 0 | 160679.3 | 19.912% | 3.150520 | 64.794% | 0.079430 | 1.129675 | 0.320185 | 0.824728 | 79.212% |
| 2 | 0 | 176994.6 | 32.087% | 2.623629 | 70.682% | 0.059328 | 1.061584 | 0.347330 | 0.799592 | 74.757% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
