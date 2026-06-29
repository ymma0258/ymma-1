# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 12.484647 | 0.000% | 0.304993 | 3.427479 | 0.142564 | 0.845209 | 88.170% |
| 1.5 | 1 | 189430.9 | 41.369% | 3.641509 | 70.832% | 0.062926 | 1.595739 | 0.368523 | 0.671618 | 65.385% |
| 2 | 1 | 198260.4 | 47.958% | 3.840128 | 69.241% | 0.067565 | 1.542855 | 0.340865 | 0.685511 | 67.094% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
