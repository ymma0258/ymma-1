# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.3 | 0.000% | 8.962482 | 0.000% | 0.291771 | 2.771462 | 0.174410 | 0.873409 | 89.560% |
| 0.25 | 0 | 143278.1 | 6.660% | 6.022589 | 32.802% | 0.162572 | 1.829003 | 0.204361 | 0.859200 | 87.628% |
| 0.5 | 0 | 149310.8 | 11.151% | 4.443165 | 50.425% | 0.109437 | 1.817444 | 0.276898 | 0.829088 | 83.776% |
| 1 | 0 | 158490.3 | 17.985% | 3.033112 | 66.158% | 0.073390 | 1.058451 | 0.242358 | 0.783931 | 77.002% |
| 2 | 0 | 172502.1 | 28.415% | 2.616123 | 70.810% | 0.055500 | 0.790072 | 0.204273 | 0.760747 | 73.476% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
