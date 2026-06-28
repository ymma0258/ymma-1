# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.5 | 0.000% | 7.760996 | 0.000% | 0.243591 | 2.411547 | 0.180304 | 0.880309 | 89.758% |
| 0.5 | 0 | 147515.7 | 10.088% | 3.966908 | 48.887% | 0.104920 | 1.463858 | 0.267592 | 0.845678 | 83.380% |
| 1 | 0 | 155007.6 | 15.679% | 2.614960 | 66.306% | 0.061735 | 0.899936 | 0.243726 | 0.792743 | 75.546% |
| 1.5 | 0 | 160830.1 | 20.025% | 2.196688 | 71.696% | 0.045226 | 0.694747 | 0.243999 | 0.760888 | 70.817% |
| 2 | 0 | 165869.5 | 23.786% | 2.080456 | 73.193% | 0.047786 | 0.608937 | 0.226811 | 0.755680 | 69.824% |
| 3 | 0 | 174844.4 | 30.483% | 1.880443 | 75.771% | 0.035105 | 0.597079 | 0.214058 | 0.729226 | 65.884% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
