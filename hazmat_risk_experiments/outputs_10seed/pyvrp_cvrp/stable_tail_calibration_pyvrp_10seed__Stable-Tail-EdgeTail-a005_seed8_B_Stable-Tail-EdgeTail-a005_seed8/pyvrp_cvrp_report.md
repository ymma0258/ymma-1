# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.4 | 0.000% | 7.315617 | 0.000% | 0.219055 | 2.414148 | 0.209763 | 0.858934 | 87.681% |
| 0.25 | 0 | 156908.0 | 6.597% | 6.041494 | 17.416% | 0.151008 | 1.835898 | 0.176815 | 0.853584 | 86.363% |
| 0.5 | 0 | 165405.3 | 12.370% | 5.216189 | 28.698% | 0.128191 | 1.881367 | 0.265947 | 0.841863 | 84.415% |
| 1 | 0 | 176231.6 | 19.725% | 3.172835 | 56.629% | 0.074980 | 1.079385 | 0.237442 | 0.785659 | 76.078% |
| 2 | 0 | 191005.3 | 29.761% | 2.478749 | 66.117% | 0.054426 | 0.687765 | 0.186394 | 0.751825 | 70.607% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
