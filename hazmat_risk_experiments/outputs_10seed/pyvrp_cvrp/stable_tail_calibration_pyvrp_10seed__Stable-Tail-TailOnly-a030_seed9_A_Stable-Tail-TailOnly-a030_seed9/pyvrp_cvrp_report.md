# PyVRP-CVRP Downstream Validation Report

- Year: `data_2021`
- Customers: `50`
- Vehicles: `5`
- Capacity: `10`
- Customer set: `A`

| beta | lambda | Cost | Cost inc. | Global risk | Risk red. | CVaR90 | Max vehicle risk | Vehicle Gini | Edge burden Gini | Top10 burden share |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 133998.0 | 0.000% | 8.786327 | 0.000% | 0.280321 | 2.504281 | 0.165653 | 0.873135 | 89.816% |
| 0.25 | 0 | 142764.0 | 6.542% | 5.794307 | 34.053% | 0.170333 | 1.835704 | 0.232778 | 0.857688 | 87.430% |
| 0.5 | 0 | 148887.0 | 11.111% | 4.365652 | 50.313% | 0.103353 | 1.645307 | 0.253420 | 0.831271 | 83.819% |
| 1 | 0 | 157617.0 | 17.626% | 2.981544 | 66.066% | 0.070604 | 1.019162 | 0.235862 | 0.781206 | 76.643% |
| 2 | 0 | 171072.3 | 27.668% | 2.392055 | 72.775% | 0.051727 | 0.717737 | 0.198429 | 0.743062 | 71.229% |

PyVRP is used only as a CVRP solver. Risk and fairness metrics are posterior evaluations of the returned routes.
