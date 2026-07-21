# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 8.561052 | 0.000% | 0.274167 | 2.421304 | 0.164301 | 0.871817 | 89.703% |
| 0.25 | 0 | 142698.3 | 6.440% | 5.873680 | 31.391% | 0.169557 | 1.807902 | 0.218341 | 0.860876 | 87.800% |
| 0.5 | 0 | 149079.6 | 11.200% | 4.462871 | 47.870% | 0.118396 | 1.645401 | 0.271616 | 0.834134 | 84.067% |
| 1 | 0 | 157730.5 | 17.653% | 2.995117 | 65.015% | 0.071928 | 1.071381 | 0.245935 | 0.778913 | 76.501% |
| 2 | 0 | 171106.2 | 27.630% | 2.496936 | 70.834% | 0.056221 | 0.710723 | 0.175968 | 0.752780 | 72.465% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
