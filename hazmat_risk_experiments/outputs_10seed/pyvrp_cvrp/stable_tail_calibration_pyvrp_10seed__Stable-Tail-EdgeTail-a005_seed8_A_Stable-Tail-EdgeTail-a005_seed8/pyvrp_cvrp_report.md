# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134198.2 | 0.000% | 7.959810 | 0.000% | 0.249456 | 2.599517 | 0.195791 | 0.871164 | 88.871% |
| 0.25 | 0 | 143257.4 | 6.751% | 5.467659 | 31.309% | 0.157394 | 1.641392 | 0.194311 | 0.858363 | 87.019% |
| 0.5 | 0 | 149759.6 | 11.596% | 3.890545 | 51.123% | 0.106090 | 1.226248 | 0.204650 | 0.822944 | 81.721% |
| 1 | 0 | 158809.6 | 18.340% | 2.907749 | 63.470% | 0.071740 | 0.773168 | 0.152949 | 0.784431 | 76.268% |
| 2 | 0 | 173759.4 | 29.480% | 2.209915 | 72.237% | 0.043827 | 0.673011 | 0.211237 | 0.741945 | 69.551% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
