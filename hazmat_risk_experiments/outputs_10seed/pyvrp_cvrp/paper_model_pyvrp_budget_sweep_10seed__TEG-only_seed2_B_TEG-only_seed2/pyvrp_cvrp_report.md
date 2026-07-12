# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `B`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 147397.1 | 0.000% | 9.410592 | 0.000% | 0.282871 | 3.430597 | 0.283864 | 0.839710 | 87.482% |
| 0.25 | 0 | 157058.0 | 6.554% | 7.853281 | 16.548% | 0.221616 | 2.657886 | 0.262532 | 0.830903 | 85.940% |
| 0.5 | 0 | 166175.3 | 12.740% | 6.845613 | 27.256% | 0.182149 | 2.217058 | 0.209306 | 0.816924 | 83.992% |
| 1 | 0 | 179253.7 | 21.613% | 4.886055 | 48.079% | 0.116174 | 1.850982 | 0.303651 | 0.775459 | 78.323% |
| 2 | 0 | 200218.9 | 35.836% | 3.957164 | 57.950% | 0.078302 | 1.599347 | 0.289072 | 0.733801 | 72.703% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
