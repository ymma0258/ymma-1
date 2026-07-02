# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 9.261776 | 0.000% | 0.267855 | 2.627362 | 0.138775 | 0.857044 | 89.183% |
| 0.5 | 0 | 150308.8 | 12.173% | 5.431597 | 41.355% | 0.162586 | 1.610452 | 0.179143 | 0.830945 | 84.563% |
| 1 | 0 | 160937.3 | 20.105% | 3.905087 | 57.837% | 0.105940 | 1.338075 | 0.244476 | 0.786946 | 78.431% |
| 1.5 | 0 | 168992.5 | 26.116% | 3.433756 | 62.926% | 0.088983 | 1.075101 | 0.272737 | 0.767343 | 75.466% |
| 2 | 0 | 176304.5 | 31.573% | 2.815839 | 69.597% | 0.059097 | 0.979209 | 0.292257 | 0.726915 | 70.048% |
| 3 | 0 | 188186.8 | 40.440% | 2.849552 | 69.233% | 0.051059 | 0.969232 | 0.306878 | 0.733308 | 70.592% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
