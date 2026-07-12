# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.8 | 0.000% | 7.555509 | 0.000% | 0.224652 | 2.513652 | 0.211241 | 0.858207 | 88.543% |
| 0.25 | 0 | 142070.6 | 5.814% | 5.804128 | 23.180% | 0.168886 | 1.793156 | 0.217639 | 0.848845 | 87.773% |
| 0.5 | 0 | 148219.4 | 10.393% | 4.133174 | 45.296% | 0.119181 | 1.149607 | 0.158450 | 0.825875 | 83.837% |
| 1 | 0 | 157747.8 | 17.490% | 3.180660 | 57.903% | 0.089373 | 0.953196 | 0.185885 | 0.794481 | 78.935% |
| 2 | 0 | 170619.5 | 27.077% | 2.341965 | 69.003% | 0.056786 | 0.757501 | 0.237285 | 0.735628 | 70.817% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
