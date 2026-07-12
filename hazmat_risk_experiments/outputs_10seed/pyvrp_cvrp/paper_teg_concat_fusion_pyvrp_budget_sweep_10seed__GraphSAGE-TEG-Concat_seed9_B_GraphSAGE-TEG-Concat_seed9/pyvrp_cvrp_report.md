# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147197.4 | 0.000% | 8.563966 | 0.000% | 0.255431 | 3.066689 | 0.247504 | 0.882327 | 90.081% |
| 0.25 | 0 | 159210.4 | 8.161% | 7.403225 | 13.554% | 0.221335 | 2.739897 | 0.281008 | 0.878807 | 89.027% |
| 0.5 | 0 | 168871.3 | 14.724% | 4.823792 | 43.673% | 0.131208 | 1.849881 | 0.320085 | 0.860517 | 84.786% |
| 1 | 0 | 180625.3 | 22.710% | 3.362582 | 60.736% | 0.075172 | 1.400758 | 0.340718 | 0.832071 | 79.404% |
| 2 | 0 | 198221.6 | 34.664% | 2.869581 | 66.492% | 0.058859 | 1.267010 | 0.359635 | 0.808448 | 75.542% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
