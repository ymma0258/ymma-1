# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134264.5 | 0.000% | 8.847788 | 0.000% | 0.284565 | 2.727024 | 0.186160 | 0.873445 | 89.694% |
| 0.25 | 0 | 142781.2 | 6.343% | 6.090060 | 31.169% | 0.178348 | 1.917940 | 0.229572 | 0.862803 | 88.121% |
| 0.5 | 0 | 149279.4 | 11.183% | 4.391336 | 50.368% | 0.107784 | 1.591716 | 0.260049 | 0.828750 | 83.546% |
| 1 | 0 | 157983.6 | 17.666% | 2.929245 | 66.893% | 0.070807 | 1.012231 | 0.260049 | 0.776166 | 76.101% |
| 2 | 0 | 171266.0 | 27.559% | 2.486430 | 71.898% | 0.055779 | 0.701797 | 0.203302 | 0.748642 | 71.949% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
