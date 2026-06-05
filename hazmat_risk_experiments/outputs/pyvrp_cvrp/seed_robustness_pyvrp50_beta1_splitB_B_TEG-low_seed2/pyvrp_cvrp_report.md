# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146531.2 | 0.000% | 9.269797 | 0.000% | 0.247355 | 3.278217 | 0.273786 | 0.841051 | 88.017% |
| 1 | 0 | 179518.6 | 22.512% | 5.118267 | 44.786% | 0.112740 | 1.818982 | 0.235688 | 0.783883 | 79.415% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
