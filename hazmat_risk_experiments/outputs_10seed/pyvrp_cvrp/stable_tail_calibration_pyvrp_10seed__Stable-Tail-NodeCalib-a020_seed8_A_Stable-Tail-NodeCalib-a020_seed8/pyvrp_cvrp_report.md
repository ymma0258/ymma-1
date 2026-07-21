# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 134064.6 | 0.000% | 7.878914 | 0.000% | 0.230362 | 2.257554 | 0.164737 | 0.870340 | 88.873% |
| 0.25 | 0 | 142975.4 | 6.647% | 5.460959 | 30.689% | 0.163049 | 1.694913 | 0.221276 | 0.859800 | 86.947% |
| 0.5 | 0 | 149465.8 | 11.488% | 4.194817 | 46.759% | 0.122638 | 1.572147 | 0.258093 | 0.833334 | 83.235% |
| 1 | 0 | 158482.6 | 18.214% | 2.868812 | 63.589% | 0.064883 | 0.777865 | 0.151340 | 0.786837 | 76.465% |
| 2 | 0 | 173373.2 | 29.321% | 2.266783 | 71.230% | 0.049636 | 0.690303 | 0.184866 | 0.749760 | 70.374% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
