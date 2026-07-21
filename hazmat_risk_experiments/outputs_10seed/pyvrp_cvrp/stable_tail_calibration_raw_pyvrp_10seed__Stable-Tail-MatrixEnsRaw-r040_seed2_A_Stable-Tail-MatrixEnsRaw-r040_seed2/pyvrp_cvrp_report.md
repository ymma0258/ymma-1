# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.3 | 0.000% | 5.395670 | 0.000% | 0.179142 | 1.649179 | 0.190339 | 0.879160 | 90.201% |
| 0.25 | 0 | 142374.8 | 6.093% | 3.736531 | 30.749% | 0.109481 | 1.182309 | 0.223648 | 0.869852 | 88.312% |
| 0.5 | 0 | 148492.2 | 10.651% | 2.892597 | 46.390% | 0.085072 | 0.982539 | 0.241119 | 0.855385 | 85.580% |
| 1 | 0 | 157500.0 | 17.364% | 1.942423 | 64.000% | 0.053836 | 0.757533 | 0.329908 | 0.813048 | 79.164% |
| 2 | 0 | 171839.1 | 28.049% | 1.764577 | 67.296% | 0.041468 | 0.732836 | 0.349839 | 0.796715 | 76.516% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
