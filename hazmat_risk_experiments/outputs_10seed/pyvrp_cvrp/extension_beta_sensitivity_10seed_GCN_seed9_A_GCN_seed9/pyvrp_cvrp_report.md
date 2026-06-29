# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133997.6 | 0.000% | 7.630782 | 0.000% | 0.219914 | 2.316810 | 0.174649 | 0.864607 | 89.123% |
| 0.5 | 0 | 148407.4 | 10.754% | 4.251567 | 44.284% | 0.126213 | 1.324055 | 0.228920 | 0.832922 | 84.199% |
| 1 | 0 | 157030.0 | 17.189% | 2.788783 | 63.454% | 0.073211 | 0.901917 | 0.248515 | 0.759534 | 74.940% |
| 1.5 | 0 | 163708.2 | 22.172% | 2.601738 | 65.905% | 0.063352 | 0.791332 | 0.227140 | 0.751449 | 73.651% |
| 2 | 0 | 170606.1 | 27.320% | 2.509491 | 67.114% | 0.051740 | 0.713980 | 0.208984 | 0.741777 | 72.108% |
| 3 | 0 | 181807.3 | 35.680% | 2.101618 | 72.459% | 0.038902 | 0.633268 | 0.196647 | 0.705652 | 66.985% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
