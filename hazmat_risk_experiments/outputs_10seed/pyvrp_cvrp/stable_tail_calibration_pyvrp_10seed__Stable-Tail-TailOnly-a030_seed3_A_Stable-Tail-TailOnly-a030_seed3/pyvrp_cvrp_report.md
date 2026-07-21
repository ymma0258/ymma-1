# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.2 | 0.000% | 7.150177 | 0.000% | 0.213537 | 2.254423 | 0.190844 | 0.875604 | 89.149% |
| 0.25 | 0 | 141474.4 | 5.579% | 4.846561 | 32.218% | 0.139897 | 1.627857 | 0.257684 | 0.860311 | 86.959% |
| 0.5 | 0 | 147082.1 | 9.764% | 3.844915 | 46.226% | 0.110190 | 1.373610 | 0.233855 | 0.840742 | 83.995% |
| 1 | 0 | 154506.2 | 15.305% | 2.295991 | 67.889% | 0.058392 | 0.689529 | 0.229893 | 0.761050 | 73.080% |
| 2 | 0 | 165934.6 | 23.833% | 2.095364 | 70.695% | 0.050581 | 0.714953 | 0.271321 | 0.749135 | 70.940% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
