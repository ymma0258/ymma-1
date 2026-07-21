# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.299306 | 0.000% | 0.264944 | 2.285663 | 0.146133 | 0.873184 | 89.811% |
| 0.25 | 0 | 142063.3 | 6.019% | 6.130073 | 26.138% | 0.186868 | 1.930046 | 0.219634 | 0.869477 | 88.572% |
| 0.5 | 0 | 147852.1 | 10.339% | 4.003812 | 51.757% | 0.101999 | 1.192260 | 0.198643 | 0.838942 | 83.240% |
| 1 | 0 | 156376.6 | 16.701% | 2.887894 | 65.203% | 0.065270 | 0.996454 | 0.250323 | 0.791935 | 76.730% |
| 2 | 0 | 169570.5 | 26.547% | 2.333082 | 71.888% | 0.046422 | 0.730490 | 0.231281 | 0.758737 | 71.613% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
