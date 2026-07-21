# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 6.961144 | 0.000% | 0.224622 | 2.030083 | 0.170177 | 0.876455 | 89.701% |
| 0.25 | 0 | 142413.1 | 6.280% | 4.504726 | 35.288% | 0.131334 | 1.559130 | 0.260542 | 0.862048 | 87.159% |
| 0.5 | 0 | 148503.3 | 10.825% | 3.835783 | 44.897% | 0.113849 | 1.460015 | 0.271710 | 0.852742 | 85.482% |
| 1 | 0 | 157667.3 | 17.664% | 2.647074 | 61.974% | 0.072644 | 0.941219 | 0.289524 | 0.813328 | 79.412% |
| 2 | 0 | 171815.0 | 28.222% | 2.287874 | 67.134% | 0.052815 | 0.927383 | 0.341746 | 0.792023 | 75.991% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
