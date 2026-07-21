# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146997.5 | 0.000% | 6.224065 | 0.000% | 0.186338 | 2.160167 | 0.257565 | 0.870036 | 88.931% |
| 0.25 | 0 | 155375.8 | 5.700% | 5.220886 | 16.118% | 0.134216 | 1.758206 | 0.254527 | 0.864045 | 87.945% |
| 0.5 | 0 | 163238.9 | 11.049% | 4.306917 | 30.802% | 0.108712 | 1.840599 | 0.314968 | 0.854636 | 85.878% |
| 1 | 0 | 174936.2 | 19.006% | 3.334757 | 46.422% | 0.085622 | 1.264404 | 0.279608 | 0.840250 | 82.801% |
| 2 | 0 | 192427.0 | 30.905% | 2.475065 | 60.234% | 0.062049 | 0.949004 | 0.292881 | 0.804642 | 77.126% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
