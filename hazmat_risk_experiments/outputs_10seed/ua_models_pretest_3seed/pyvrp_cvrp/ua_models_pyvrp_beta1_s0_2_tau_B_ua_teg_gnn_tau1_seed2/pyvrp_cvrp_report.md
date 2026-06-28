# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 146220.7 | 0.000% | 18.722302 | 0.000% | 0.091259 | 5.667117 | 0.189797 | 0.816098 | 86.898% |
| 1 | 0 | 189720.3 | 29.749% | 10.795999 | 42.336% | 0.049640 | 3.278930 | 0.191686 | 0.759913 | 78.422% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
