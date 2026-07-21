# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.039021 | 0.000% | 0.246553 | 2.351330 | 0.171374 | 0.871281 | 88.977% |
| 0.25 | 0 | 142377.6 | 6.254% | 5.241284 | 34.802% | 0.147899 | 1.720230 | 0.239424 | 0.854237 | 86.333% |
| 0.5 | 0 | 148548.0 | 10.858% | 4.119897 | 48.751% | 0.114724 | 1.464754 | 0.239069 | 0.834193 | 83.232% |
| 1 | 0 | 157049.9 | 17.203% | 2.870056 | 64.298% | 0.072592 | 0.776476 | 0.162113 | 0.782033 | 75.999% |
| 2 | 0 | 171301.2 | 27.839% | 2.588266 | 67.804% | 0.055545 | 0.775594 | 0.206543 | 0.771491 | 73.935% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
