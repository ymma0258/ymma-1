# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134464.6 | 0.000% | 8.156402 | 0.000% | 0.255542 | 2.262169 | 0.157824 | 0.865649 | 88.470% |
| 0.25 | 0 | 143469.1 | 6.697% | 5.423828 | 33.502% | 0.155044 | 1.700057 | 0.229941 | 0.851496 | 86.252% |
| 0.5 | 0 | 149615.2 | 11.267% | 4.004869 | 50.899% | 0.115693 | 1.379606 | 0.256293 | 0.818026 | 81.568% |
| 1 | 0 | 158871.3 | 18.151% | 2.835989 | 65.230% | 0.075452 | 0.925473 | 0.275186 | 0.770879 | 74.980% |
| 2 | 0 | 173239.9 | 28.837% | 2.198804 | 73.042% | 0.050097 | 0.823189 | 0.297764 | 0.721146 | 68.012% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
