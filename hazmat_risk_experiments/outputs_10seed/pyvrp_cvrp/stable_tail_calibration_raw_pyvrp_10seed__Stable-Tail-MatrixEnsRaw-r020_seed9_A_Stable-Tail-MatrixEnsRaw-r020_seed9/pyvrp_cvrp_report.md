# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134065.0 | 0.000% | 6.731924 | 0.000% | 0.214479 | 2.011699 | 0.182875 | 0.872193 | 89.610% |
| 0.25 | 0 | 143135.1 | 6.765% | 4.585327 | 31.887% | 0.130901 | 1.480163 | 0.221500 | 0.855936 | 87.228% |
| 0.5 | 0 | 149538.3 | 11.542% | 3.501777 | 47.983% | 0.087166 | 1.405351 | 0.279538 | 0.826249 | 83.408% |
| 1 | 0 | 158540.6 | 18.257% | 2.380413 | 64.640% | 0.057230 | 0.846795 | 0.262917 | 0.778571 | 76.302% |
| 2 | 0 | 172243.0 | 28.477% | 1.948961 | 71.049% | 0.043020 | 0.583275 | 0.219732 | 0.747314 | 71.791% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
