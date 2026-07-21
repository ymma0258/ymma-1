# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134397.8 | 0.000% | 8.591063 | 0.000% | 0.275200 | 2.780631 | 0.198895 | 0.868862 | 88.965% |
| 0.25 | 0 | 143281.9 | 6.610% | 5.226686 | 39.161% | 0.144886 | 1.617806 | 0.224539 | 0.849011 | 86.157% |
| 0.5 | 0 | 149820.1 | 11.475% | 4.247467 | 50.559% | 0.112911 | 1.565451 | 0.234635 | 0.822969 | 82.871% |
| 1 | 0 | 159007.6 | 18.311% | 3.057918 | 64.406% | 0.074286 | 1.066752 | 0.255589 | 0.779586 | 76.582% |
| 2 | 0 | 173783.1 | 29.305% | 2.446051 | 71.528% | 0.052412 | 0.762005 | 0.217648 | 0.743066 | 71.265% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
