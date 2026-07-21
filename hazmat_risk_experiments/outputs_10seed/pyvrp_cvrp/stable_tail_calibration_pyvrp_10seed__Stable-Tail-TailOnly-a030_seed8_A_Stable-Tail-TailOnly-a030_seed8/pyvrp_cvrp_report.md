# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.125273 | 0.000% | 0.249587 | 2.396423 | 0.175590 | 0.872079 | 89.094% |
| 0.25 | 0 | 142269.3 | 6.173% | 5.477329 | 32.589% | 0.154771 | 1.738365 | 0.222149 | 0.858186 | 86.890% |
| 0.5 | 0 | 148128.9 | 10.546% | 4.271311 | 47.432% | 0.123522 | 1.607177 | 0.262725 | 0.836881 | 83.676% |
| 1 | 0 | 156740.5 | 16.972% | 2.812108 | 65.391% | 0.070077 | 0.847411 | 0.208212 | 0.779965 | 75.687% |
| 2 | 0 | 170477.6 | 27.224% | 2.443974 | 69.921% | 0.049851 | 0.752867 | 0.217473 | 0.765370 | 72.948% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
