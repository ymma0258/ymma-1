# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146730.9 | 0.000% | 11.804737 | 0.000% | 0.300314 | 3.657283 | 0.192179 | 0.853547 | 88.510% |
| 1 | 0 | 181286.6 | 23.550% | 5.382158 | 54.407% | 0.111221 | 1.829739 | 0.274089 | 0.791527 | 79.937% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
