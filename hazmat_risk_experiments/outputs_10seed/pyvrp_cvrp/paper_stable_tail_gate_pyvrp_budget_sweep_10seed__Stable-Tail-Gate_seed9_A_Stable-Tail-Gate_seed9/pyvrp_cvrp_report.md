# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.262832 | 0.000% | 0.214478 | 2.256441 | 0.187274 | 0.862138 | 88.359% |
| 0.25 | 0 | 142731.8 | 6.518% | 5.315619 | 26.811% | 0.147154 | 1.712461 | 0.217632 | 0.848368 | 86.323% |
| 0.5 | 0 | 148752.2 | 11.011% | 4.017663 | 44.682% | 0.113009 | 1.659822 | 0.291538 | 0.816587 | 82.445% |
| 1 | 0 | 157039.0 | 17.195% | 2.696626 | 62.871% | 0.068863 | 0.775230 | 0.168295 | 0.756877 | 74.213% |
| 2 | 0 | 170681.3 | 27.376% | 2.214769 | 69.505% | 0.049365 | 0.706906 | 0.235240 | 0.716250 | 68.403% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
