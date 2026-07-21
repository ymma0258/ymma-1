# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.1 | 0.000% | 9.036499 | 0.000% | 0.284930 | 3.390865 | 0.312327 | 0.876185 | 89.778% |
| 0.25 | 0 | 156390.8 | 6.246% | 7.686870 | 14.935% | 0.234174 | 2.933410 | 0.332821 | 0.874292 | 89.134% |
| 0.5 | 0 | 164860.5 | 12.000% | 6.053011 | 33.016% | 0.172772 | 2.308378 | 0.281927 | 0.859061 | 86.612% |
| 1 | 0 | 176943.1 | 20.208% | 4.462635 | 50.615% | 0.120488 | 1.802609 | 0.309363 | 0.842339 | 83.157% |
| 2 | 0 | 195369.4 | 32.726% | 3.647351 | 59.638% | 0.091175 | 1.735191 | 0.364938 | 0.827246 | 80.123% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
