# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134331.2 | 0.000% | 8.668027 | 0.000% | 0.280360 | 2.599452 | 0.178366 | 0.860486 | 88.437% |
| 0.25 | 0 | 143095.8 | 6.525% | 6.421366 | 25.919% | 0.200469 | 1.916294 | 0.207058 | 0.855078 | 88.021% |
| 0.5 | 0 | 149587.3 | 11.357% | 4.942985 | 42.975% | 0.144451 | 1.736905 | 0.248186 | 0.832992 | 85.149% |
| 1 | 0 | 159065.4 | 18.413% | 3.236583 | 62.661% | 0.081106 | 1.105025 | 0.250813 | 0.775263 | 77.055% |
| 2 | 0 | 173243.8 | 28.968% | 2.543356 | 70.658% | 0.049136 | 0.841565 | 0.247011 | 0.725515 | 70.232% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
