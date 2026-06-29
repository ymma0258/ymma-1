# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 10.349132 | 0.000% | 0.206600 | 3.488600 | 0.245546 | 0.882281 | 90.439% |
| 1 | 0 | 171608.6 | 16.955% | 3.314177 | 67.976% | 0.057357 | 1.074298 | 0.267773 | 0.795089 | 74.941% |
| 2 | 0 | 183149.8 | 24.820% | 2.732708 | 73.595% | 0.043835 | 0.992333 | 0.258558 | 0.756307 | 69.363% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
