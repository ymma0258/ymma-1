# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 9.099935 | 0.000% | 0.284265 | 2.994060 | 0.219721 | 0.881188 | 90.226% |
| 1 | 0 | 180194.2 | 22.806% | 4.064539 | 55.334% | 0.094769 | 1.476661 | 0.310923 | 0.838335 | 81.378% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
