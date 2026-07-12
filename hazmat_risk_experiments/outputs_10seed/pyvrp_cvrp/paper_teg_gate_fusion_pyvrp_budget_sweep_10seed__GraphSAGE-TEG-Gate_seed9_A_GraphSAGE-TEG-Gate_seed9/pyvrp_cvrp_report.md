# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.7 | 0.000% | 7.398015 | 0.000% | 0.211704 | 2.257178 | 0.206133 | 0.877914 | 89.395% |
| 0.25 | 0 | 141519.9 | 5.614% | 4.857945 | 34.334% | 0.139708 | 1.580991 | 0.250212 | 0.860442 | 86.393% |
| 0.5 | 0 | 146347.4 | 9.216% | 3.515930 | 52.475% | 0.102068 | 1.553960 | 0.312989 | 0.825954 | 81.819% |
| 1 | 0 | 153642.9 | 14.661% | 2.625634 | 64.509% | 0.057741 | 0.802117 | 0.184432 | 0.777014 | 75.646% |
| 2 | 0 | 164071.6 | 22.444% | 1.786993 | 75.845% | 0.029922 | 0.522938 | 0.190545 | 0.705308 | 64.265% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
