# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.1 | 0.000% | 8.627143 | 0.000% | 0.286214 | 2.482079 | 0.178659 | 0.883837 | 89.609% |
| 0.25 | 0 | 144020.0 | 7.479% | 5.896818 | 31.648% | 0.187959 | 1.878863 | 0.227318 | 0.875524 | 86.665% |
| 0.5 | 0 | 150628.1 | 12.411% | 4.849864 | 43.784% | 0.114138 | 1.816546 | 0.307867 | 0.858391 | 84.101% |
| 1 | 0 | 161057.3 | 20.194% | 3.450079 | 60.009% | 0.080246 | 1.222165 | 0.296082 | 0.818146 | 77.643% |
| 2 | 0 | 176697.0 | 31.865% | 2.887023 | 66.536% | 0.065950 | 1.254741 | 0.350084 | 0.800902 | 74.876% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
