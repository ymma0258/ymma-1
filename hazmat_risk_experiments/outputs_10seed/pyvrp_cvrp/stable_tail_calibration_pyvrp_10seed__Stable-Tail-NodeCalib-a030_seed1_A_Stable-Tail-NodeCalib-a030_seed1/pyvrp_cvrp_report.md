# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 9.448574 | 0.000% | 0.309610 | 2.689935 | 0.157834 | 0.874344 | 89.947% |
| 0.25 | 0 | 141799.3 | 5.822% | 6.268093 | 33.661% | 0.189740 | 1.824567 | 0.188392 | 0.863148 | 87.536% |
| 0.5 | 0 | 147681.2 | 10.211% | 4.784170 | 49.366% | 0.121314 | 1.722554 | 0.239201 | 0.843750 | 84.262% |
| 1 | 0 | 156188.6 | 16.560% | 3.254496 | 65.556% | 0.073046 | 1.044396 | 0.205721 | 0.795740 | 77.265% |
| 2 | 0 | 168756.9 | 25.940% | 2.700248 | 71.422% | 0.056006 | 0.780273 | 0.194690 | 0.770108 | 72.912% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
