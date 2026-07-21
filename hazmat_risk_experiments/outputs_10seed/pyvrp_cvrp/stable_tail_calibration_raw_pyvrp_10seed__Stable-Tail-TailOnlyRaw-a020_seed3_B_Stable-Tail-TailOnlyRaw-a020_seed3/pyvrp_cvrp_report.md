# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147463.8 | 0.000% | 7.417465 | 0.000% | 0.231743 | 2.596130 | 0.254522 | 0.872379 | 89.500% |
| 0.25 | 0 | 155549.9 | 5.483% | 6.152672 | 17.052% | 0.164050 | 2.262633 | 0.272418 | 0.869805 | 88.676% |
| 0.5 | 0 | 163129.3 | 10.623% | 4.994203 | 32.670% | 0.128629 | 1.997327 | 0.294654 | 0.859798 | 86.547% |
| 1 | 0 | 175345.4 | 18.907% | 3.654004 | 50.738% | 0.092380 | 1.608167 | 0.332983 | 0.839868 | 82.595% |
| 2 | 0 | 191798.7 | 30.065% | 2.879664 | 61.177% | 0.072686 | 1.223464 | 0.295670 | 0.816211 | 78.298% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
