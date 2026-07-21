# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147263.7 | 0.000% | 7.087449 | 0.000% | 0.224889 | 2.510153 | 0.264948 | 0.875101 | 90.254% |
| 0.25 | 0 | 156271.4 | 6.117% | 5.657536 | 20.175% | 0.150559 | 1.931613 | 0.270163 | 0.871704 | 88.884% |
| 0.5 | 0 | 163964.4 | 11.341% | 4.547589 | 35.836% | 0.119728 | 1.404773 | 0.221600 | 0.857488 | 86.317% |
| 1 | 0 | 173678.1 | 17.937% | 2.762721 | 61.020% | 0.061009 | 0.923580 | 0.232447 | 0.817057 | 79.502% |
| 2 | 0 | 187657.6 | 27.430% | 2.364971 | 66.632% | 0.047360 | 0.792465 | 0.252918 | 0.800961 | 76.590% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
